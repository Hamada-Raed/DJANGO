from django.urls import path , include

urlpatterns = [
    path ('', include( 'myapp.urls')),
    path ('<int:id>' , include( 'myapp.urls')),
    path ('hamada/', include('myapp.urls')),
    path ('hello_world/', include('myapp.urls')),
    path ('<int:id>/<str:color>', include('myapp.urls')),
]