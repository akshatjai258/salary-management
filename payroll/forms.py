from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import ( User,Employee)


class HrSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields='__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_hr = True
        if commit:
            user.save()
        return user


class EmployeeSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields='__all__'

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user)
        return user

