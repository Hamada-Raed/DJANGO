from django.shortcuts import render, redirect
from django.http import HttpResponse
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
        User.objects.create(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        return redirect ('/')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        request.session['username'] = User.objects.last().username
        this_user = User.objects.get(email=request.POST['email'])
        return redirect ('/display') 

def display(request): 
    context = {
        'username' : request.session['username'],
        'courses': Course.objects.all()
    }

    return render(request, 'display.html', context) 

def logout(request): 
    request.session.flush()
    return redirect('/')

def cancel(request): 
    return render(request, 'display.html')

def create(request):
    return render(request, 'new.html')

def create_course(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create')
    else:
        request.session['user_id'] = User.objects.last().id
        print (request.session['user_id'])
        Course.objects.create(
            name = request.POST['name'], 
            day = request.POST['day'], 
            number = request.POST['number'],
            desc =request.POST['desc'], 
            Insturctor= request.POST['instructor'],
            user = User.objects.get(id=request.session['user_id']), 
        )
        return redirect('/display')

def details(request, course_id):
    context = {
        'courses' : Course.objects.get(id = course_id),
        'user' : User.objects.all(),
    }
    return render(request, 'details.html', context)

def delete(request, course_id):
    dell = Course.objects.get(id = course_id)
    dell.delete() 
    return redirect('/display')

def edit_show(request, course_id):
    context = {
        'courses' : Course.objects.get(id=course_id) 
    }
    return render(request,'delEdi.html',context)

def edit(request, course_id): 
    errors = Course.objects.course_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit_show/'+course_id)
    else:
        selected = Course.objects.get(id=course_id)
        selected.name = request.POST['name']
        selected.Insturctor = request.POST['insturctor']
        selected.day = request.POST['day']
        selected.number = request.POST['number']
        selected.desc = request.POST['desc']
        selected.save()
        return redirect('/display')




    