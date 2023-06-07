

from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),
    path('/blogs', include('users.urls')),
    path('/surveys', include('surveys.urls')),
]
