from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']

        x= User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        return render(request, 'homepage.html')
    else:
        return render(request, 'signup.html')

def loginuser(request):
    if(request.method == 'POST'):
        username1 = request.POST['username']
        password1 = request.POST['password']
        x= auth.authenticate(username=username1,password=password1)
        if x is None:
            return render(request, 'signup.html')
        else:
            return render(request, 'homepage.html')
    else:
        return render(request, 'login.html')

