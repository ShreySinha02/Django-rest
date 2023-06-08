from django.contrib import admin
from .models import Students
# Register your models here.
@admin.register(Students)
class studentsAdmin(admin.ModelAdmin):
    list_display=["name","roll","city"]
