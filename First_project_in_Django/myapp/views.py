from django.shortcuts import render , HttpResponse ,redirect    
from django.http import JsonResponse
def index(request):
    return redirect("/blogs") 

def root(request): 
    return HttpResponse ('placeholder to later display a list of all blogs" with a method named "index"')

def new(request): 
    return HttpResponse ('display the string "placeholder to display a new form to create a new blog" with a method named "new"')

def create(request): 
    return redirect ('/')

def show(request, number): 
    return HttpResponse (f'placeholder to display blog number {number}')  

def edit(request, number): 
    return HttpResponse (f"placeholder to edit blog {number}") 

def destroy(request,number):
    return redirect ('/') 

def json_method(request): 
    return JsonResponse({"title": "The first blod"}, 
    {'content': 'JSON response from redirected_method'})


