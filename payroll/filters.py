import django_filters
from django_filters import CharFilter,ChoiceFilter
from django.contrib.auth.models import User
from .models import Employee


class search_user(django_filters.FilterSet):
    class Meta:
        model=User
        fields = ['username']
        


class search_doctor(django_filters.FilterSet):
    Address=CharFilter(field_name='address',lookup_expr='icontains',label='Address')
    employee=CharFilter(field_name='full_name',lookup_expr='icontains',label='Employee')
    class Meta:
        model=Employee
        fields = ['employee','Address']
        
        
    