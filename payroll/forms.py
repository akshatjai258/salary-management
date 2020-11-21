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

class UserUpdateForm(forms.ModelForm):
	
  email = forms.EmailField()
  first_name=forms.CharField()
  last_name=forms.CharField()	
  class Meta:
      model = User
      fields = ['username', 'email','first_name','last_name']

class EmplyeeUpdateForm(forms.ModelForm):
	profile_pic = forms.ImageField(widget=forms.FileInput,)
	class Meta:
		model = Employee
		fields = ['profile_pic','phone','address']

