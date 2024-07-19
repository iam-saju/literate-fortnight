from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            print(user)  # For debugging
            
            if user is not None:
                login(request, user)
                messages.success(request, "You're plugged in!")
                return redirect('home')
            else:
                messages.error(request, 'yo invalid data')
        else:
            messages.error(request, 'Please provide both username and password.')
        
        return redirect('home')
    
    return render(request, 'home.html', {})

def base(req):
    return render(req,'base.html')

def login_user(req):
    pass

def signup(req):
    
    return render(req,'register.html')

def logout_user(req):
    logout(req)
    messages.success(req,'yo plugged out/')
    return redirect('home')
