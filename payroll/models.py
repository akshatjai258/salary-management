from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)

    
class Leave(models.Model):
    date = models.DateField(help_text="date of leave")
    reason = models.CharField(help_text="reason of leave", max_length=255)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
  


class Holiday(models.Model):
    date = models.DateField(help_text="a holiday of the year",null=True)
    holiday_name = models.CharField(default="National holiday",null=True, help_text="the name of the holiday", max_length=50)
    description = models.CharField(default="nationally celebrated",null=True, help_text="the reason for the holiday", max_length=255)

    def __str__(self):
        return self.holiday_name
        

class Contact(models.Model):
	sno=models.AutoField(primary_key=True)
	name=models.CharField(max_length=250)
	email=models.CharField(max_length=250)
	content=models.CharField(max_length=300)
	
	
	def __str__(self):
		return "message from "+self.name

class hrProfile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50,null = True)
    profile_pic=models.ImageField(upload_to='images/profile', blank = True, default='images/profile/default2.jpeg')
    phone=PhoneNumberField(blank = True)
    address=models.TextField(blank = True, max_length=255)
    company_name = models.CharField(max_length=255,blank=True,null=True)
    year_of_registration = models.DateField(null=True)
    

  
class Employee(models.Model):
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    
    
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    parent_hr = models.ForeignKey(hrProfile,null=True,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50,null = True)
    profile_pic=models.ImageField(upload_to='images/profile', blank = True, default='images/profile/default2.jpeg')
    phone=PhoneNumberField(blank = True,null=True)
    address=models.TextField(blank = True, max_length=255,null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True)
    post = models.CharField(max_length=50,null = True)
    department = models.CharField(max_length=50,null=True)
    epf_deduction = models.IntegerField(default=0)
    esi_deduction = models.IntegerField(default=0)
    allowances_per_month = models.IntegerField(default=0)
    base_salary = models.IntegerField(default=0)


    
