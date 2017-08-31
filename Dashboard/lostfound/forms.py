from django import forms
from .models import Lost
from .models import Found
from django.forms import ModelForm


class LostForm(ModelForm):

    class Meta:
        model = Lost
        fields = ['Item_Name','Item_Image','Description','Last_Seen']



class FoundForm(ModelForm):
    class Meta:
        model = Found
        fields=['Item_Name','Item_Image','Description','Found_on']