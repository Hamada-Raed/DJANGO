from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('display/<user_id>/', views.display),
    path('add_book/<user_id>', views.add_book),
    # path('logout', views.logout)

    
]