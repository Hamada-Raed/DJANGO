from django.shortcuts import render , redirect
import random 

def index(request):
    # x = request.POST['user_name']
    if 'guess_num' not in request.session: 
        request.session['guess_num'] = random.randint(1, 100)
    if 'text' not in request.session: 
        request.session['text'] ='' 
    if 'color' not in request.session:
        request.session['color']=''
    if 'count' not in request.session:
        request.session['count']= 0
    if 'tries' not in request.session: 
        request.session['tries']= 5
    if 'name' not in request.session: 
        request.session['name'] = 'x'

    content = {
        'guessNumber' : request.session['guess_num'],
        'color_box' : request.session['color'] ,
        'text_box' : request.session['text'],
        'counter' : request.session['count'],
        'num_of_try' : request.session['tries'],
        'username':  request.session['name'],
    } 
    
    return render (request, 'index.html' , content) 

def guess(request):
    content = {
        'counter' : request.session['count']+1,
        'username':  request.session['name'],
    }  
    num_from_form = int(request.POST['num'])
    if num_from_form == request.session['guess_num']:
        return render (request, 'win.html', content)
    elif num_from_form > request.session['guess_num']:
        request.session['text'] = 'TO HIGH' 
        request.session['color'] = 'red' 
    elif num_from_form < request.session['guess_num']:
        request.session['text'] = 'TO LOW' 
        request.session['color'] = 'red'  
    # Number of tries and check if it is 5 print massage to tell the user, You lose
    
    if request.session['count'] == 5:
        request.session['text'] = 'YOU LOSE'
    
    request.session['tries'] -=1
    request.session['count']+=1   
    return redirect ('/') 

def destory(request): 
    del request.session['guess_num'] 
    del request.session['text']
    del request.session['color']
    del request.session['count']
    del request.session['tries']
    del request.session['name']
    return redirect ('/') 





