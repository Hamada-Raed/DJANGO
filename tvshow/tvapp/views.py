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

def show_page(request, show_id):
    context = {
        "shows" : show.objects.get(id=show_id),
    }
    return render(request, 'show.html', context)

def edit_page(request, edit_id): 
    context = {
        "update" : show.objects.get(id=edit_id),  
    }
    return render (request, 'edit_page.html', context)

def edit(request):
    name = request.POST['title']
    network = request.POST['network']
    desc = request.POST['desc']
    release_date = request.POST['release_date']
    return redirect("/edit_page/<edit_id>")