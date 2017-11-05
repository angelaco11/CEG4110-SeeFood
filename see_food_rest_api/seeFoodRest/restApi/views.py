from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProcessedImage
from .serializers import ProcessedImageInitalSerializer
from .serializers import ProcessedImageReturnImagesSerializer
from rest_framework import status


# Create your views here.
class ImageList(APIView):

    def get(self, request, last_sync_date=None, id=None):

        if last_sync_date != None and id == None:
            imageDataInitAll = ProcessedImage.objects.all()
            serializer = ProcessedImageInitalSerializer(imageDataInitAll, many=True)
            return Response(serializer.data)
        elif last_sync_date == None and id != None:
            imageDataID = ProcessedImage.objects.get(id=id)
            serializer = ProcessedImageReturnImagesSerializer(imageDataID, many=False)

            try:
                #You are going to have to change the path for this to test it.
                with open(r'C:\Users\Matt\Desktop\PythonProjects\see_food_rest_api\seeFoodRest\restApi\cookies.jpg', "rb") as f:
                    return HttpResponse(f.read(), content_type="image/jpeg")
            except IOError:
                red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
                response = HttpResponse(content_type="image/jpeg")
                red.save(response, "JPEG")
                return response


    def post(self, request):
        serializer = ProcessedImageInitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
