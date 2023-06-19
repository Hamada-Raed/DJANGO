from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_course', views.add_course),
    path ('remove/<course_id>', views.remove),
    path ('no/<course_id>', views.no),
    path ('yes/<course_id>', views.yes),
]
