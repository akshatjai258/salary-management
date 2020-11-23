from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import auth
from django.contrib.auth.forms import UserCreationForm
from .models import Leave, Holiday, Employee,hrProfile,Contact
from django.views.generic import TemplateView,CreateView,DetailView
from .forms import *
from .filters import *
from .templatetags import doctor_extras
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.contrib.auth import get_user_model

User = get_user_model()






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


def HrProfile(request,pk):
    hrprofile=get_object_or_404(hrProfile,id=pk)
  
    context={
        'hr':hrprofile,
    }
    return render(request,'profile/hrProfile.html',context)


# def profile(request):
#   if request.method == 'POST':
#       u_form = UserUpdateForm(request.POST, instance=request.user)
#       d_form = EmployeeUpdateForm(request.POST,request.FILES,instance=request.user.doctor)
#       if u_form.is_valid() and d_form.is_valid():
#           u_form.save()
#           d_form.save()
#           messages.success(request, f'Your account has been updated!')
#           return redirect("home")

#   else:
#       u_form = UserUpdateForm(instance=request.user)
#       d_form = UpdateProfileForm(instance=request.user.doctor)

#   context = {
#       'u_form': u_form,
#       'd_form': d_form
#   }

#   return render(request, 'profile/editemployee.html', context)



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
    employees=Employee.objects.all()
    myFilter1=search_doctor(request.GET,queryset=employees)

    employees=myFilter1.qs
    paginated_list=Paginator(employees,2)
    page_number=request.GET.get('page')
    employee_page_obj=paginated_list.get_page(page_number)
    context={'employees':employees,'myFilter1':myFilter1,'employee_page_obj':employee_page_obj}
    return render(request,'payroll/employee_list.html',context)

def EmployeeProfile(request,pk):
    employee = Employee.objects.get(id=pk)
    return render(request,'payroll/employee_each.html',{'employee':employee})


def HrSignup(request):
    if request.method == 'GET':
        form = HrCreationForm()
        return render(request,'registration/signup_form.html',{'form':form})
    else:
        form = HrCreationForm(request.POST)
        
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            company_name = form.cleaned_data["company_name"]
            year_of_registration = form.cleaned_data["year_of_registration"]
            address = form.cleaned_data["address"]
            phone_number = form.cleaned_data["phone_number"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            full_name = str(first_name)+" "+str(last_name)

            if password1 == password2:
                if User.objects.filter(username = username).exists():
                    messages.info(request,"username already taken")
                    return render(request,'registration/signup_form.html',{'form':form})
                elif User.objects.filter(email = email).exists():
                    messages.info(request,"email already taken")
                    return render(request,'registration/signup_form.html',{'form':form})
                else:
                    user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,is_hr=True)   
                    user.save()
                    hr = hrProfile(user = user,full_name=full_name,phone_number=phone_number,address=address,company_name=company_name,year_of_registration=year_of_registration)
                    hr.save()
                    messages.success(request,'company registered sucessfully')
                    print("company created")

                return redirect('login')
            else:
                messages.info(request,"enter same password for both fields")
                return render(request,'registration/signup_form.html',{'form':form})
        
        else :
            messages.info(request,"please make sure you have filled all the fields correctly")
            return render(request,'registration/signup_form.html',{'form':form})

def EmployeeSignup(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = EmployeeCreationForm()
            return render(request,'registration/signup_employee.html',{'form':form})
        else:
            form = EmployeeCreationForm(request.POST)
            
            if form.is_valid():
                username = form.cleaned_data["username"]
                email = form.cleaned_data["email"]
                password1 = form.cleaned_data["password1"]
                password2 = form.cleaned_data["password2"]
                phone_number = form.cleaned_data["phone_number"]
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                full_name = str(first_name)+" "+str(last_name)
                post = form.cleaned_data["post"]
                department = form.cleaned_data["department"]
                epf_deduction = form.cleaned_data["epf_deduction"]
                esi_deduction = form.cleaned_data["esi_deduction"]
                allowances_per_month = form.cleaned_data["allowances_per_month"]
                base_salary = form.cleaned_data["base_salary"]

                if password1 == password2:
                    if User.objects.filter(username = username).exists():
                        messages.info(request,"username already taken")
                        return render(request,'registration/signup_employee.html',{'form':form})
                    elif User.objects.filter(email = email).exists():
                        messages.info(request,"email already taken")
                        return render(request,'registration/signup_employee.html',{'form':form})
                    else:
                        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,is_employee=True)
                        user.save()
                        current_hr = request.user
                        parent_hr = current_hr.hrprofile
                        employee = Employee(user = user,full_name=full_name,phone_number=phone_number,parent_hr=parent_hr,epf_deduction=epf_deduction,esi_deduction=esi_deduction,department=department,post=post,allowances_per_month=allowances_per_month,base_salary=base_salary,)
                        messages.success(request,'employee added sucessfully')
                        print("employee added")
                    
                    return redirect('login')

                else:
                    messages.info(request,"enter same password for both fields")
                    return render(request,'registration/signup_employee.html',{'form':form})
            
            else :
                messages.info(request,"please make sure you have filled all the fields correctly")
                return render(request,'registration/signup_employee.html',{'form':form})
    
    else:

        messages.info(request,"please be logged in as a company admin to add employees")
        return redirect('login')



                        





                
                

            
        

        
       
       