from django.shortcuts import render ,redirect
from .models import Book, Author

def book(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request, "book.html", context)

def add_book(request):
    new_book = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')

def delete_book(request):
    delete_book = Book.objects.get(id=16)
    delete_book.delete()
    return redirect ('/')

def book_info(request, book_id):
    context = {
        'books' : Book.objects.get(id = book_id),
        'authors' : Book.objects.get(id = book_id).books_authors.all(),
        'all_authors' : Author.objects.all(), 
    }
    return render(request, "book_info.html", context)

def author(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render (request, 'author.html',context)

def add_author(request):
    new_author = Author.objects.create(first_name  = request.POST['first_name'], last_name = request.POST['last_name'], notes =request.POST['notes'] )
    return redirect('/author')

def author_info(request, author_id):
    context = {
        'authors' : Author.objects.get(id = author_id),
        'books' : Author.objects.get(id = author_id).books.all(),
        'all_books' : Book.objects.all(),
    }
    return render(request, "author_info.html", context)