from django.shortcuts import render
from .models import show
import datetime
def index(request): 
    context = {
        'shows' : show.objects.all()
    }
    return render(request, 'index.html',context) 

def add_show(request):
    name = request.POST['title']
    show.objects.create(
        title = name,
        network= request.POST['network'],
        desc= request.POST['desc'],
    )
    return redirect('/')
