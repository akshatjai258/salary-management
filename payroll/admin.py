from django.contrib import admin
from .models import Holiday,Leave,Employee,Contact

# Register your models here.

admin.site.register(Holiday)
admin.site.register(Leave)
admin.site.register(Employee)
admin.site.register(Contact)
