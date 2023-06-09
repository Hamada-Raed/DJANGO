from django.shortcuts import render , redirect 
from .models import users
def index(request):
    content = {
        "all_the_users" : users.objects.all(),
    }
    return render (request, 'index.html',content)

def adduser(request):
    new_user = users.objects.create(name = str(request.POST['name']) , email_address = str(request.POST['email_address']), age = int(request.POST['age']))
    new_user.save()
    content = {
        "all_the_users" : users.objects.all(),
    }
    return render (request, 'index.html',content)