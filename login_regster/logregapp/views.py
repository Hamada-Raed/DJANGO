from django.shortcuts import render

def index(request): 
    return render(request, 'index.html') 
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
        print(pw_hash)
        request.session['username'] = fname + " "+ lname
        request.session['status']="Registered"
        User.objects.create(first_name=fname, last_name=lname,email=email, password=pw_hash)
    return redirect("/success")

def success(request): 
    return render(request, 'success.html')