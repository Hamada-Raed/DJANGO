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
        return redirect ('/classes') 

# to display the all classes
def classes(request): 
    context = {
        'user' : request.session['username'],
        'courses' : Course.objects.all(),
    }
    
    return render(request, 'classes.html', context)

def logout(request): 
    request.session.flush()
    return redirect('/')

# to display the page (create/add course)
def new_course(request):
    return render(request, 'new_course.html')

def add_course(request):
    request.session['user_id'] = User.objects.last().id 
    Course.objects.create(
        name = request.POST.get('name_course', False),
        day= request.POST.get('day', False),
        number= request.POST.get('number',False),
        desc= request.POST.get('desc',False),
        Insturctor= request.POST.get('insturctor',False), 
        user = User.objects.get(id=request.session['user_id']),
    )
    return redirect('/classes')
def details(request, course_id):
    context = {
        'courses' : Course.objects.get(id=course_id),
        'user' : User.objects.all(),
    }  
    return render(request, 'details.html', context)

def edit(request, course_id):
    selected = Course.objects.get(id=course_id) 
    selected.name = request.POST.get('name_course', False)    
    context = {
        'course': Course.objects.get(id=course_id) 
        }
    return render(request, 'edit.html', context)

def delete(request, course_id):
    dell = Course.objects.get(id= course_id)
    dell.delete() 
    return redirect('/classes')