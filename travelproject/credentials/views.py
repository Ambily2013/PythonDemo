from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render, redirect

def login(request):

     if request.method =='POST':
         username=request.POST['username']
         password=request.POST['password']
         user=auth.authenticate(username=username,password=password)

         if user is not None:
             auth.login(request,user)
             return redirect('/')
         else:
             message.info(request,"Invalid credentials")
             return redirect('login')
     return render(request,"login.html")


def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        pwd=request.POST['password']
        cpwd=request.POST['password1']

        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username is already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email ID is already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=pwd,first_name=fname,last_name=lname,email=email)
                user.save();
                return redirect('login')


        else:
            messages.info(request,"Password is Not Matching")
            return redirect('register')

        return redirect('/')


    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
