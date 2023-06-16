from django.urls import path 
from . import views

urlpatterns = [
    path('', views.book),
    path('add_book', views.add_book),
    path('delete_book', views.delete_book),
    path('author', views.author), 
    path ('add_author' ,views.add_author), 
    path('book_info/<book_id>', views.book_info),
    path('author_info/<author_id>', views.author_info),
    path('add_author_to_book/<books_id>', views.add_author_to_book),
    path('author_info1', views.author_info1),
  
    
]
