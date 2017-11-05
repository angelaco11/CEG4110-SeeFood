from rest_framework import serializers
from .models import ProcessedImage

class ProcessedImageInitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcessedImage
        fields = ['id', 'upper', 'lower']

class ProcessedImageReturnImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcessedImage
        fields = ['file_path']
