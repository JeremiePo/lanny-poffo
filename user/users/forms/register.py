from django import forms

class RegisterForm(forms.Form):
    pseudo = forms.CharField(max_length=255)
    mail = forms.CharField(max_length=255)

    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)
