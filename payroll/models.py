from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)


class Department(models.Model):
    dept_name = models.CharField( help_text="The department to which the employee belongs", max_length=100)
    base_salary = models.IntegerField(default=0, help_text="the base salary of employees in this department or project")

    def __str__(self):
        return self.dept_name
    
class Post(models.Model):
    post_name = models.CharField( help_text="The employees post", max_length=100)
    base_salary = models.IntegerField(default=0, help_text="the base salary of employees having this post regardless of the department")

    def __str__(self):
        return self.post_name

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
        

class Employee(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50,null = True)
    profile_pic=models.ImageField(upload_to='images/profile', blank = True, default='images/profile/default2.jpeg')
    phone=PhoneNumberField(blank = True)
    address=models.TextField(blank = True, max_length=255)
    department = models.ForeignKey(Department,null=True,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,null=True,on_delete=models.CASCADE)

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
    department = models.ForeignKey(Department,null=True,on_delete=models.CASCADE)
