from django import forms
from .models import AccomodationForm
from django.forms import ModelForm


class RequestForm(ModelForm):

    class Meta:
        model = AccomodationForm
        fields = ['Name1','Gender1','Name2','Gender2','Name3','Gender3','Purpose']

