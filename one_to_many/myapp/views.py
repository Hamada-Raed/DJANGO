from django.shortcuts import render
from .models import Author , Book
def index(request):
    new_author = Author.objects.create(name ='Hamada')
    contant = {
        'author_in_template' : new_author.name
    }
    return render (request ,'index.html', contant)
  
