from django import forms
class SigninForm(forms.Form):
    username=forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    


