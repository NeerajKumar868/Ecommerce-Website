from tkinter import Widget

from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from .models import Profile




class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]
        help_texts = {
            'username': None,
        }
class ProfileForm(forms.ModelForm):
    roles=(('admin',"Admin"),('customer',"Customer"))
    role=forms.ChoiceField(widget=forms.RadioSelect,choices=roles)
    class Meta:
        model=Profile
        fields=['mobile_no']
