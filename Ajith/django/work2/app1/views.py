from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.into(request,'Email is exist')
                return redirect(signup)
            else:
                user=User.objects.create_user(username=username,
                password=password,email=email,first_name=first_name,last_name=last_name)
                user.set_password(password)
                user.save()
                print('success')
                return redirect('login_user')
        else:
            messages.info(request,'Both password are not matching')
            return redirect(signup)
    else:
        print('no post method')
        return render(request,'signup.html')
# def login_user(request):
#         if request.method=='POST':
