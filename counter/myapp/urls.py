from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index),
    path('delet',views.delet) ,
    path ('addtwo',views.addtwo),
    path ('reset',views.reset),
    path ('addnum',views.add_num),
]
