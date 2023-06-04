from django.shortcuts import redirect

def index(request): 
    if request.method == "GET":
    	print("a GET request is being made to this route")
    if request.method == "POST":
        print("a POST request is being made to this route")
    	
