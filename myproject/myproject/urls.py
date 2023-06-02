
from django.urls import path , include

urlpatterns = [
    path ('', include( 'myapp.urls')),
    path ('hi/', include ('hiapp.urls')), 
    path ('hamada', include('myapp2.urls')),
]
