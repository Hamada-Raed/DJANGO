from django.shortcuts import render, redirect
from .models import show
def index(request):
    context = {
        'shows' : show.objects.all()
    }
    return render (request, 'index.html', context)

def GoToAddShow(request):
    return render (request, 'add_show.html')

def add_show(request):
    show.objects.create(
        name = request.POST['title'],
        network = request.POST['network'], 
        release_date = request.POST['date'], 
        desc = request.POST['desc'],
    )
    return redirect('/')

def GoBack(request):
    return redirect('/') 

def show_page(request):
    context = {
        "details" : show.objects.get(id=show.id).show.all()
    }
    return render(request, 'show.html', context)

    