from django.db import models

# Create your models here.
class AccomodationForm(models.Model):
    genders = (('Male', 'Male'), ('Female', 'Female'))
    Name1 = models.CharField(max_length=100)
    Gender1 = models.CharField(max_length=10, choices=genders)
    Name2 = models.CharField(max_length=100)
    Gender2 = models.CharField(max_length=10, choices=genders)
    Name3 = models.CharField(max_length=100)
    Gender3 = models.CharField(max_length=10, choices=genders)
    Purpose=models.CharField(max_length=500)

    def __str__(self):
        return self.Name1



