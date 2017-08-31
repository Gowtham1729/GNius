from django.contrib import admin
from .models import Folder,File,Course

admin.site.register(Course)
admin.site.register(File)
admin.site.register(Folder)