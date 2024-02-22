from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# A class for sign-in/Login validation


class Validation():

    def __init__(self, username, password, mail, repeat_password=""):
        assert(len(username) != 0 and "User username should not be empty")
        assert(len(password) != 0 and "user Pasword should not be empty")
        assert(len(mail) != 0 and "User Mail should not be empty")

        self.username = username  
        self.password = password  
        self.mail = mail
        self.repeat_password = repeat_password


    def validate_user_length(self, string, len_number):
        if len(string) < len_number:
            raise Exception

    def is_password_same(self):
        if self.password != self.repeat_password:
            raise Exception

    def authentification(self):
        user = authenticate(username=self.username, password=self.password, mail=self.mail)
        if user is None:
            raise Exception
        else:
            return user
        
    def already_exist(self):
        user = User.objects.get(username=self.username)


valid = Validation("a", "b", "c")
valid2 = Validation("a", "b", "c")
valid = valid2