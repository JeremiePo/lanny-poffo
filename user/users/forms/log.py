from django import forms

class LoginForm(forms.Form):
    pseudo = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
