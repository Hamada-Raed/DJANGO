from django.urls import path ,include 
from . import views
urlpatterns = [
    path('', views.index),
    path('<name>/', views.hello), 
    path('<name>/<int:age>', views.hello),
    path('<name>/<int:age>/<int:id>', views.hello)  
]
