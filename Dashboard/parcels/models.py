from django.db import models


class Post(models.Model):
    company = models.CharField(max_length=20)
    receiver = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    room = models.CharField(max_length=10, default="None")
    choices = (
        ('Aibaan', 'Aibaan'), ('Beauki', 'Beauki'), ('Chimair', 'Chimair'), ('Duven', 'Duven'), ('Emiet', 'Emiet'),
        ('Firpeal', 'Firpeal'))
    hostelname = models.CharField(max_length=256, default="None", choices=choices)

    def __str__(self):
        return self.receiver + "-" + self.company
from django.db import models