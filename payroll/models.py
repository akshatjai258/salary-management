from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(blank = False, help_text="The department to which the employee belongs")
    base_salary = models.IntegerField(default=0, help_text="the base salary of employees in this department or project")

    def __str__(self):
        return self.dept_name
    
class Post(models.Model):
    post_name = models.CharField(blank = False, help_text="The employees post")
    base_salary = models.IntegerField(default=0, help_text="the base salary of employees having this post regardless of the department")

    def __str__(self):
        return self.post_name

class Leave(models.Model):
    date = models.DateField(help_text="date of leave")
    reason = models.CharField(help_text="reason of leave", blank = False)
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
  


class Holiday(models.Model):
    date = models.DateField(help_text="a holiday of the year")
    holiday_name = models.CharField(default="National holiday", help_text="the name of the holiday", max_length=50)
    description = models.CharField(default="nationally celebrated", help_text="the reason for the holiday", max_length=255)

    def __str__(self):
        return self.holiday_name
        

class Employee(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	profile_pic=models.ImageField(upload_to='images/profile', blank = True, default = 'images/profile/default2.jpeg')
    phone=PhoneNumberField(blank = False)
    Address=models.TextField(blank = True, max_length=255)

