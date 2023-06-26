from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('classes', views.classes), 
    path('logout', views.logout),
    path('cancel', views.classes),
    path('new_course', views.new_course), 
    path('add_course', views.add_course),
    path('details/<course_id>', views.details),
    path('edit/<course_id>', views.edit),
    path('delete/<course_id>', views.delete),
]
