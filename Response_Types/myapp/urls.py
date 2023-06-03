from django.urls import path 
from . import views
urlpatterns = [
    path ('', views.index ),
    path('another_route/', views.another_method),
    path('redirected_route/', views.redirected_method),
]
