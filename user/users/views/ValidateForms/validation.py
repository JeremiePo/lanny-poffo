from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class Validation(): # Base class for validation of forms

    def __init__(self, username, password, mail, repeat_password):
        assert(len(username) != 0 and "User username should not be empty")
        assert(len(password) != 0 and "user Pasword should not be empty")
        assert(len(mail) != 0 and "User Mail should not be empty")
        assert(len(repeat_password) != 0 and "User Mail should not be empty")
        self.username = username  
        self.password = password  
        self.mail = mail
        self.repeat_password = repeat_password


    def is_password_same(self):
        pass
        
    def validate_min_length(self, string, len_number):
        pass

    def validate_max_length(self, string, len_number):
        pass

    def already_exists(self):
        pass
