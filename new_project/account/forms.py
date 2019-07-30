from django import forms
from .models import Account

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['userID', 'password', 'nick']
        widgets ={
            'password' : forms.PasswordInput()
        }

class LoginForm(forms.Form):
    userId = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)

