from django.contrib import admin
from testapp.models import student

class studentAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','marks','add']
admin.site.register(student,studentAdmin)
# Register your models here.
