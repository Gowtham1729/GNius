from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from os import path
from datetime import datetime


class Course(models.Model):
    course_title = models.CharField(max_length=6)
    course_code = models.CharField(max_length=3, null=True)
    Sun = models.BooleanField()
    Mon = models.BooleanField()
    Tue = models.BooleanField()
    Wed = models.BooleanField()
    Thu = models.BooleanField()
    Fri = models.BooleanField()
    Sat = models.BooleanField()
    From = models.TimeField()
    To = models.TimeField()

    def __str__(self):
        return self.course_title + ' - ' + self.course_code

    def courses_today(self, num):
        c = {7:self.Sun, 1:self.Mon, 2:self.Tue, 3:self.Wed, 4:self.Thu, 5:self.Fri, 6:self.Sat}
        return c[num]
    @property
    def is_present(self):
        now = datetime.now().isoweekday()
        return Course.courses_today(self, now)


class Folder(models.Model):
    folder = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.folder


class File(models.Model):
    Title = models.CharField(max_length=150)
    Stream = models.CharField(max_length=150, null=True)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Type = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    report = models.BooleanField(default=False)

    def filename(self):
        return path.basename(self.file.name)

    def __str__(self):
        return self.Title
