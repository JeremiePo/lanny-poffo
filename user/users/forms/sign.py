from django import forms

class Sign(forms.Form):
    pseudo = forms.CharField()
    mail = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # repeat_password = forms.CharField(widget=forms.PasswordInput)
