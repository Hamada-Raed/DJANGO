from django.shortcuts import render, HttpResponse 

def index (request) : 
    return HttpResponse ('hi') 

def hello(request, id ): 
    return HttpResponse ('MY ID IS '  + str(id)) 

def hamada(request): 
    return HttpResponse ('I AM TRYING TO GET FAMILIER WITH ROUTING IN DJANGO') 

def hello_world(request): 
    return HttpResponse ("Hello World") 

def color(request, id , color): 
    return HttpResponse ( f" THE ID IS {str(id)} AND THE COLOR IS {color}")