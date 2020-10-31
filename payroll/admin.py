from django.contrib import admin
from .models import Holiday,Leave,Department,Post,Employee

# Register your models here.

admin.site.register(Holiday)
admin.site.register(Leave)
admin.site.register(Department)
admin.site.register(Post)
admin.site.register(Employee)
