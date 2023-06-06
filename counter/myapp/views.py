from django.shortcuts import render ,redirect

def index(request): 
    if 'count' not in request.session: 
        request.session['count'] = 1  
    else : 
        request.session['count'] += 1 
    content = {
        'counter' : request.session['count']
    }
    return render (request, 'index.html', content)  

def delet(request):
    del request.session['count'] 
    return redirect ('/') 

def addtwo(request): 
    request.session['count'] +=1 
    return redirect ('/')

def reset(request): 
    request.session['count'] = 0 
    return redirect ('/') 

def add_num(request): 
    request.session['count'] +=  int(request.POST['num'])-1
    return redirect ('/')