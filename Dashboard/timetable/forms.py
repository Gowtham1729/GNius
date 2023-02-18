from django import forms
from .models import CoursesReg


class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = CoursesReg
        fields = ['course1', 'course2', 'course3', 'course4', 'course5', 'course6', 'course7', 'course8', 'course9',
                  'course10']
