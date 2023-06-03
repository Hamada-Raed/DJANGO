from django.shortcuts import render

def index(request): 
    return render (request, 'index.html') 

def hello(request, name, age,id): 
    context = {
        'htmlname' : name,
        'myage' : age, 
        'myid': id,
        "pets": ["Bruce", "Fitz", "Georgie"] , 
        'myskills' : {
            'python' : "90%",
            'CSS' : "99%",
            'JS' : '80%'
        }
    }
    return render (request, 'helloname.html', context )