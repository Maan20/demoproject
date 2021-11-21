from django import db
from django.shortcuts import render, redirect
from .models import School
# Create your views here.
def index(request):
    if request.method=="POST":
        status=request.POST.get('status')
        print(status)
        data=School.objects.filter(id=status)
        return render(request, 'index.html',{'data':data})
    data=School.objects.all().order_by('-id')
    return render(request, 'index.html',{'data':data})

def Forms(request):    
    if request.method=="POST":
        name=request.POST.get('name')
        marks=request.POST.get('marks')
        subject=request.POST.get('subject')
        School.objects.create(subject=subject,name=name,marks=marks)
        return redirect('index')
    return render(request, 'forms.html')

def delete(request):
    return  redirect('index')

def DropDownSearch(request):
    data=School.objects.filter(id=1)
    return render(request, 'index.html',{'data':data})