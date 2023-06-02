from django.urls import path 
from . import views
urlpatterns = [
    path ('', views.index ),
    path ('hi/', views.hi), 
    path ('hamada/',views.hamada)
]
