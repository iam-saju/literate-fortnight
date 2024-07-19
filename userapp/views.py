from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import signupform,addform
from .models import record
# Create your views here.


def home(request):
    records=record.objects.all()


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # For debugging
        
        if user is not None:
            login(request, user)
            messages.success(request, "You're plugged in!")
            return redirect('home')
        else:
            messages.error(request, 'yo invalid data')
            redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def base(req):
    return render(req,'base.html')

def login_user(req):
    pass

def signup(req):
    if req.method=='POST':
        form=signupform(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(req,user)
            messages.success(req,'yo welcome to the crib!')
            redirect('home')
    else:
        form=signupform()
        
    return render(req,'register.html',{'frm':form})
    



def logout_user(req):
    logout(req)
    messages.success(req,'yo plugged out/')
    return redirect('home')



def customer(req,pk):
    if req.user.is_authenticated:
        customer=record.objects.get(id=pk)
        return render(req,'record.html',{'record':customer})
    
    else:
        messages.success(req,'yo login !/')
        return redirect('home')


def add(req):
    if req.method=='POST':
        form=addform(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,f'yo  welcome to the hood!')
            redirect('home')
      
    else:
        form=addform()
    return render(req,'add.html',{'frm':form})

def update(req,pk):
    if req.user.is_authenticated:

        customer=record.objects.get(id=pk)
        form=addform(req.POST or None,instance=customer)
        if req.method=='POST':
            if form.is_valid():
                form.save()
                messages.success(req,f'yo homie just got updated!')
                return redirect('home')
                
        else:
            return render(req,'update.html',{'frm':form})
    
    else:
        messages.success(req,'yo login !/')
        return redirect('home')





def delete(req,pk):

    if req.user.is_authenticated:
        customer=record.objects.get(id=pk)
        customer.delete()
        messages.success(req,'yo deleted succesfuly !/')
        return redirect('home')
    else:
        messages.success(req,'yo login required !/')
        return redirect('home')

   


