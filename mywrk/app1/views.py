from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import *
# Create your views here.
from app1.models import *

# def home(request):
    # d={'name':'Alex','age':20}
    # d=student.objects.all()
    # return render(request,'home.html',{'d':d})
def home(request):
    d=EMP.objects.all()
    return render(request,'emp.html',{'t':d})

def index(request):
    return HttpResponse("hello welcome to this page")

def form1(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'form1.html',{'form':form})    