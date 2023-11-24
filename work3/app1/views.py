from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#Create your views here.
def home (request):
    return render(request,"index.html")
def register(request):
    if request.method=="POST":
       first_name=request.POST['first name']
       last_name=request.POST['last name']
       username=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       confim_password=request.POST['confirm password']
       if password==confim_password:
          if User.objects.filter(username=username).exists():
              messages.info(request, 'Email is exist')
              return redirect(register)
          else:
            user=User.objects.create_user(username=username, password=password, email=email, first_name=first_name,last_name=last_name)
            user.set_password(password)
            user.save()
            print("success")
            return redirect(login_user)
       else:
          print("no post method")
    return render(request, 'register.html')
def login_user(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       user=authenticate(username=username, password=password)
       if user is not None:
           login(request, user)
           return redirect(home)
       else:
          return redirect(login_user)
    return render(request, "login.html")
def logout_user(request):
    logout (request)
    return redirect(login_user)