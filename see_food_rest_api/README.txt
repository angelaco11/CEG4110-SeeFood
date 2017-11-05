*This currently does not use the file path of the id provided.

*Make sure python manage.py runsever has been entered before attempting to access the rest

*You will need to change the file path for the image to test the code submitted to test the image functionality...
Currently it points to C:\Users\Matt\Desktop\PythonProjects\see_food_rest_api\seeFoodRest\restApi\cookies.jpg.
Then you will need to supply an id=x without supplying an sd= in the url

*You can make posts as there is a method to accept post (but I would not as of right now as I haven't tested it much really I think we just take json data right now iirc)

*The correct type of urls are as follows
url(r'^admin/', admin.site.urls)            For this one the admin name is Matt and the password is Theadmin4321 (you can add yourself or change ownerships if you want to add or change dummy data)
url(r'processedImages/sd=(?P<last_sync_date>\w{8})/$', views.ImageList.as_view(),),		Form is currently... localhost:8000/processImages/sd=12345678    The last part of the url must 8 numbers 
url(r'processedImages/id=(?P<id>\w{0,1000})/$', views.ImageList.as_view(),)			Form is currently... localhost:8000/processImages/id=1  	The id arg must be between 0-1000

*There are some changes we are going to have to these urls but for the sake of it working, it works.

*If anyone has any questions about anything ask me and I'll do my best to clarify anything iff I know
