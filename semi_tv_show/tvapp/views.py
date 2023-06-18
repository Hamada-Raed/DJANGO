from django.shortcuts import render, redirect
from .models import show
from django.contrib import messages

def index(request):
    context = {
        'all_shows' : show.objects.all()
    }
    return render (request, 'index.html',context)

# to display the page to add a show
def show_page(request):
    return render (request, 'add_show.html')

# to add a new show
def add(request):
    errors = show.objects.basic_validator(request.POST)
    if len(errors) > 0: 
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/show_page')
    else:
        show.objects.create(
            title=request.POST['title'], 
            network=request.POST['network'],
            release_date=request.POST['release_date'], 
            desc=request.POST['desc']
        )
    return redirect("/")

# to show the details for the show
def display_show(request, show_id):
    context = {
        "shows": show.objects.get(id=show_id)
    }
    return render(request, "display_show.html", context)
    
# to dispaly the  show page
def edit_show(request, show_id):
    context = {
        "shows": show.objects.get(id=show_id),
        "date": str(show.objects.get(id=show_id).release_date)
    }
    return render(request, "edit_show.html", context)

# to edit the show
def edit(request, show_id):
    selected = show.objects.get(id= show_id)
    if request.POST['title']:
        selected.title = request.POST['title']
    
    if request.POST['network']:
        selected.network = request.POST['network']
    
    if request.POST['release_date']:
        selected.release_date = request.POST['release_date']
    
    if request.POST['desc']:
        selected.description = request.POST['desc']
    selected.save()
    return redirect("/")

# delete a show 
def delete_show(request, show_id):
    show.objects.get(id=show_id).delete()
    return redirect("/")

