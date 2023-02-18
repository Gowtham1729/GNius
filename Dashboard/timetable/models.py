from django.db import models
from terashare.models import Course
from profiles.models import UserProfile


class CoursesReg(models.Model):
    user_profile = models.OneToOneField(UserProfile)
    course1 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course1', null=True)
    course2 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course2', null=True)
    course3 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course3', null=True)
    course4 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course4', null=True)
    course5 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course5', null=True)
    course6 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course6', null=True)
    course7 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course7', null=True)
    course8 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course8', null=True)
    course9 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course9', null=True)
    course10 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course10', null=True)

    def __str__(self):
        return self.user_profile.user.username


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateField()
    event_time_from = models.TimeField()
    event_time_to = models.TimeField()

    def __str__(self):
        return self.event_name
