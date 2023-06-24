from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request): 
    return render (request, 'index.html')

def register(request): 
    errors = User.objects.Register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else: 
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
        print(pw_hash)
        request.session['username'] = fname + " " + lname
        request.session['status']="Registered"
        User.objects.create(fname=fname, lname=lname,email=email, password=pw_hash) 
        return redirect ('/') 


