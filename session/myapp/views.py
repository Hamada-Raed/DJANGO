from django.shortcuts import render , redirect

def index(request):
    return render (request, 'index.html') 

def test(request): 
    request.session['name'] = request.POST['name'] 
    return redirect ('/show') 

def show(request): 
    return render (request, 'show.html')