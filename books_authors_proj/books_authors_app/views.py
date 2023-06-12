from django.shortcuts import render ,redirect
from .models import Book, Author
def index(request):
   
    content = {
        'all_books' : Book.objects.all(),

    }
    return render (request , 'index.html',content)

def add_book(request): 
    new_book = Book.objects.create(title = request.POST['name'], desc = request.POST['description'])
    content = {
        'all_books' : Book.objects.all(), 
        'all_books' : new_book
    }
    return redirect ('/')

def view_book(request):
    return render (request , 'view_book.html')