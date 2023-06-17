from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index),
    path('show_page', views.show_page), 
    path('add', views.add),
    path('display_show/<show_id>', views.display_show), 
    path('edit_show/<show_id>', views.edit_show),
    path('edit/<show_id>', views.edit),
    path('delete_show/<show_id>', views.delete_show)
]