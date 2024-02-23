from django import forms
from .models import *

class SigninForm(forms.Form):
    username=forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class SettingForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['bio','profileimg','location']


    


