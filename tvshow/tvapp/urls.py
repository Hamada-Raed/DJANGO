from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('GoToAddShow', views.GoToAddShow),
    path('add_show', views.add_show), 
    path('GoBack', views.GoBack), 
    path('show_page/<show_id>', views.show_page), 
    path('edit_page/<edit_id>', views.edit_page), 
    path('edit', views.edit)
]
