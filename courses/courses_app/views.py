from django.shortcuts import render, redirect
from .models import Course 
from django.contrib import messages

def index(request): 
    context = {
        'courses' : Course.objects.all()
    }
    return render (request, 'index.html', context) 

def add_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)  
        return redirect ('/')
    else:
        Course.objects.create(
            name=request.POST['name'], 
        )
        return redirect("/")

def remove(request, course_id): 
    context = {
        'dell' : Course.objects.get (id = course_id)
    }
    return render (request, 'remove.html', context)

def no(request,course_id):
    if request.POST['no'] == 'No': 
        return redirect ('/')
    elif request.POST['no'] == 'Yes, I want to delete this':
        selected = Course.objects.get(id=course_id).delete()
        return redirect ('/')

    



