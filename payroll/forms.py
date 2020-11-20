from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import ( User,Employee,hrProfile)


class HrSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields=['first_name','last_name','username','email','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_hr = True
        user.save()
        hr = hrProfile.objects.create(user=user)
        return user


class EmployeeSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields=['first_name','last_name','username','email','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user)
        return user

