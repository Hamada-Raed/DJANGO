from django.shortcuts import render, redirect
from .models import Player
from  django.contrib import messages 
def index(request):
    context = {
        'players' : Player.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    errors = Player.objects.basic_vaildater(request.POST)
    
    if len (errors) > 0 : 
        for k,v in errors.items():
            messages.error(request, v)
    return redirect ('/')

    new_player = Player.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        team = request.POST['team']
    )

    return redirect('/')
