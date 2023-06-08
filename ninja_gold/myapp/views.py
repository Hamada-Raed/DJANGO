from django.shortcuts import render, redirect
import random 
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0 

    if 'count' not in request.session: 
        request.session['count'] = 0 

    if 'num' not in request.session: 
        request.session['num']= request.POST['number']

    if 'text' not in request.session: 
        request.session['text']=''
        
    request.session['text']=''
    content = {
        'gold_money' : request.session['gold'], 
        'counter' : request.session['count'], 
        'massage' : request.session['text'],
    }
    return render (request, 'index.html',content) 

def money(request):
    method = request.POST['money'] 
    if method == 'farm'or 'cave' or 'house': 
        amount = random.randint(10,20)
        request.session['gold']+=amount 
        

    elif method == 'quest':  
        amount = random.randint(0,50) 
        request.session['gold']+=amount 
    
    elif request.session['gold'] >= request.session['num'] :
        request.session['text']='YOU WIN'

    request.session['count']+=1
    response = redirect('/')
    return response

def delet(request): 
    del request.session['gold']
    response = redirect('/')
    return response
