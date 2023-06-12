from django.shortcuts import render
from .models import Author , Book
def index(request):
    new_author = Author.objects.create(name ='Hamada')
    Mahmmoud_darweah = Author.objects.create(name ='Mahmmoud darweah')
    book1 = Book.objects.create(title = "title1", author = Mahmmoud_darweah )
    book2 = Book.objects.create(title = "title2", author = Mahmmoud_darweah )
    arr = []
    for i in Book.objects.all():
        arr.append(i.author.name)

    contant = {
        'author_in_template' : Mahmmoud_darweah.name, 
        'list_of_books' : arr ,  

    }
    return render (request ,'index.html', contant)
  
