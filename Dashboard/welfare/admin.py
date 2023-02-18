from django.contrib import admin
from .models import Category, Complaint
# Register your models here.

admin.site.register(Complaint)
admin.site.register(Category)