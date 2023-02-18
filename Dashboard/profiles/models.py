from django.db import models
from django.contrib.auth.models import Permission, User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    Roll = models.CharField(max_length=8)
    programmes = (
        ('Btech', 'Btech'), ('Mtech', 'Mtech'), ('MA', 'MA'), ('Msc', 'Msc'), ('Phd', 'Phd'), ('Alumni', 'Alumni'),
        ('Staff', 'Staff'))
    Programme = models.CharField(max_length=99, choices=programmes)
    course_reg = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
