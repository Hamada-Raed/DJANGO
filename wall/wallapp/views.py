from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages

def index(request):
    return render (request, 'index.html')

#register new user
def register(request):
    errors = User.objects.regValidator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        User.objects.create(first_name=request.POST['firstname'], last_name=request.POST['lastname'], email=request.POST['email'], password=request.POST['password'])

        request.session['user_name'] = User.objects.last().first_name
        request.session['user_id'] = User.objects.last().id
        print(request.session['user_name'], request.session['user_id'])
        return redirect ('/wall')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        this_user = User.objects.get(email=request.POST['email'])
        request.session['user_name'] = this_user.first_name
        request.session['user_id'] = this_user.id
        print("login successful, redirecting to the wall")
        print("THIS USER is ", request.session['user_name'], "id = ", request.session['user_id'])
        return redirect ('/wall')


def wall(request):
    if 'user_name' not in request.session:
        return redirect('/')
    context = {
        "all_messages" : Message.objects.all(),
        "all_comments" : Comment.objects.all(),
    }
    return render(request, 'wall.html', context)

def logout(request):
        request.session.flush()
        return redirect('/')

#Methods for Messages
def postMessage(request):
    poster = User.objects.get(id=request.session['user_id'])
    Message.objects.create(mess=request.POST['message_posted'], user=poster)
    return redirect ('/wall')

def postComment(request):
    poster = User.objects.get(id=request.session['user_id'])
    on_message = Message.objects.get(id=request.POST['on_message_id'])
    Comment.objects.create(comment=request.POST['comment_posted'], poster=poster, on_message=on_message)
    return redirect ('/wall')

def deleteComment(request):
    this_message = Message.objects.get(id=request.POST['message_id'])
    this_message.delete()
    return redirect ('/wall')