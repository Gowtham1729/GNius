from django.contrib.auth.models import User
from django.db import models
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return  self.category

class Complaint(models.Model):
    Title = models.CharField(max_length=99)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Description = models.TextField(max_length=499)
    Hostel = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.Title
