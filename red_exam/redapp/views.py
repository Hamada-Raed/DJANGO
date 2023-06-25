from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

def index(request): 
    return render(request, 'index.html')

def register(request):
    errors = User.objects.regValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        User.objects.create(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        return redirect ('/')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        request.session['username'] = User.objects.last().username
        this_user = User.objects.get(email=request.POST['email'])
        return redirect ('/display') 

def display(request): 
    context = {
        'username' : request.session['username'],
        'teams': Team.objects.all()
    }

    return render(request, 'display.html', context) 

def logout(request): 
    request.session.flush()
    return redirect('/')

def dashborad(request): 
    return render(request, 'dashborad.html')

def create(request):
    return render(request, 'new.html')

def create_team(request):
    request.session['user_id'] = User.objects.last().id
    print (request.session['user_id'])
    Team.objects.create(
        team_name = request.POST['team_name'], 
        skill_level = request.POST['skill_level'], 
        game_day = request.POST['game_day'],
        user = User.objects.get(id=request.session['user_id']), 
    )
    return redirect('/display')

def details(request, team_id):
    context = {
        'teams' : Team.objects.get(id = team_id)
    }
    return render(request, 'details.html', context)

def delete(request, team_id):
    dell = Team.objects.get(id = team_id)
    dell.delete() 
    return redirect('/display')

def edit_show(request, team_id):
    context = {
        'teams' : Team.objects.get(id=team_id) 
    }
    return render(request,'delEdi.html',context)

def edit(request, team_id):
    selected = Team.objects.get(id=team_id)
    selected.team_name = request.POST['team_name']
    selected.skill_level = request.POST['skill_level']
    selected.game_day = request.POST['game_day']
    selected.save()
    print('hi')
    return redirect('/display')



    