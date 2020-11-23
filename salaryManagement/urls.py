"""salaryManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from payroll.views import SignUpView,EmployeeSignUpView,HrSignUpView,HrSignup,EmployeeSignup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payroll/', include('payroll.urls')),
    path('', views.home, name='home'),
    path('support/',views.payment,name='payment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/employee/', EmployeeSignup, name='employee_signup'),
    path('accounts/signup/hr/', HrSignup, name='hr_signup'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="main/password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), name="password_reset_complete"),
]
    


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
