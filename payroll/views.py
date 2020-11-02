from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .models import Department, Post, Leave, Holiday, Employee

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully registered")
            return redirect("/")
        
    else:
        form = UserCreationForm()

    return render(request,'payroll/register.html',{'form':form})


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request, "Successfully logged in")
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect('payroll/login')
    else:
        return render(request,'payroll/login.html')

def signout(request):
    auth.logout(request)
    messages.info(request, "successfuly logged out")
    return redirect("/")

def view_list(request):
    employees = Employee.objects.all()
    return render(request,'payroll/employee_list.html',{'employees':employees})

def view_each(request,pk):
    employee = Employee.objects.get(id=pk)
    return render(request,'payroll/employee_each.html',{'employee':employee})