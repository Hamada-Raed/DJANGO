from django.shortcuts import render, HttpResponse
def hi(request):
    return HttpResponse("HELLO, MY NAME IS HAMADA!")


def index(request):
    return HttpResponse("response from index method from root route, localhost:8000!")

def hamada(request): 
    return HttpResponse ("I AM FULL STACK DEVELOPER")
