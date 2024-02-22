from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def min_length(string, len_number):
    if len(string) < len_number:
        return ValidationError


def max_length(string, len_number):
    if len(string) > len_number:
        return ValidationError



class Validation():

    def __init__(self, username, mail):
        assert(len(username) != 0 and "Username is empty")
        assert(len(mail) != 0 and "Mail is empty")

        self.username = username  
        self.mail = mail

   

            # return render(request, "sign-in.html")

    def are_password_same(self):
        if self.password != self.repeat_password:
            raise ValidationError("Password are not the same")

    def authentification(self):
        user = authenticate(username=self.username, password=self.password, mail=self.mail)
        if user is None:
            raise ValidationError("")
        else:
            return user
        
    def already_exist(self):
        user = User.objects.get(username=self.username)
    
    def email_already_exists(self):
        if User.objects.filter(email=self.mail).exists():
            raise ValidationError("")
