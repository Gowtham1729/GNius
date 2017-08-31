from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class ToPalajWD(models.Model):
    time = models.TimeField()
    route = models.CharField(max_length=100)
    routepic = models.ImageField(name='routepic', width_field=None, height_field=None,default="images/Integrated Route Map-pagep001_6.jpg")

    def get_absolute_url(self):
        return reverse('topalaj:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.time) + '-' + self.route

class ToPalajHD(models.Model):
    time = models.TimeField()
    route = models.CharField(max_length=100)
    routepic=models.ImageField(name='routepic',width_field=None,height_field=None,default="images/Integrated Route Map-pagep001_6.jpg")

    def get_absolute_url(self):
        return reverse('topalaj:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.time) + '-' + self.route


class ToChandhkedaWD(models.Model):
    time = models.TimeField()
    route = models.CharField(max_length=100)
    routepic=models.ImageField(name='routepic',width_field=None,height_field=None,default="images/Integrated Route Map-pagep001_6.jpg")

    def get_absolute_url(self):
        return reverse('tochandkeda:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.time) + '-' + self.route

class ToChandhkedaHD(models.Model):
    time = models.TimeField()
    route = models.CharField(max_length=100)
    routepic = models.ImageField(name='routepic', width_field=None, height_field=None,default="images/Integrated Route Map-pagep001_6.jpg")

    def get_absolute_url(self):
        return reverse('tochandkeda:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.time) + '-' + self.route




