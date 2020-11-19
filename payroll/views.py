from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .models import Department, Post, Leave, Holiday, Employee
from django.views.generic import TemplateView,CreateView
from .forms import *

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class EmployeeSignUpView(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class HrSignUpView(CreateView):
    model = User
    form_class = HrSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'hr'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

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

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def view_list(request):
    employees = Employee.objects.all()
    return render(request,'payroll/employee_list.html',{'employees':employees})

def view_each(request,pk):
    employee = Employee.objects.get(id=pk)
    return render(request,'payroll/employee_each.html',{'employee':employee})