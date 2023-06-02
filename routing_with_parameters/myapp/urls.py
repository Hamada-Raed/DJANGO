from django.urls import path 

from . import views 

urlpatterns = [ 
    path ('', views.index),
    path('<int:id>', views.hello),
    path ('hamada/' , views.hamada),
    path ('hello_world/', views.hello_world),
    path ('<int:id>/<str:color>', views.color),

]

