from django.shortcuts import render,redirect

def index(request): 
    return render (request, 'index.html')

def create(request): 
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    lang_from_form = request.POST['lang']
    comment_from_form = request.POST['comment']
    context = {
    	"name_on_template" : name_from_form,
        'location_on_template' : location_from_form, 
        'lang_on_template' : lang_from_form, 
        'comment_on_template' : comment_from_form
    }
    return render (request, 'show.html' , context) 




