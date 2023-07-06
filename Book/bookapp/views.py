from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request): 
    return render(request, 'index.html')

def register(request):
    errors = User.objects.regValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        User.objects.create(
            username=request.POST['username'], 
            email=request.POST['email'],
            password=request.POST['password'])
        return redirect ('/')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        this_user = User.objects.get(email=request.POST['email'])
        return redirect ('/display/'+str(this_user.id))


def display(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id) ,
        'books' : Book.objects.all(),
    }
    return render(request, 'display.html', context)

def add_book(request, user_id): 
    errors = Book.objects.bookValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/display')
    else: 
        if request.method == 'POST':
            Book.objects.create(
                title = request.POST['title'],
                desc = request.POST['desc'],
                user = User.objects.get(id=user_id)
            )  
            return redirect('/display')

# def logout(request): 
#     del request.session['username'] 
#     return redirect('/')