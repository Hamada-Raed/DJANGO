from django.shortcuts import render , HttpResponse

def index(request):
    return HttpResponse("This is the equivelent of @app.route('/')")
