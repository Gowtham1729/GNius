from django.db import models

# Create your models here.
class Lost(models.Model):
    Item_Name = models.CharField(max_length=100)
    Item_Image=models.ImageField(default="\static\lostfound\images\empty.png")
    Description = models.TextField(max_length=500)
    Last_Seen = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.Item_Name

class Found(models.Model):
    Item_Name = models.CharField(max_length=100)
    Item_Image=models.ImageField(default="\static\lostfound\images\empty.png")
    Description = models.TextField(max_length=500)
    Found_on = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.Item_Name