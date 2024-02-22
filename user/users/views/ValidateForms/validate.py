from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class Validation(): # Base class for validation of forms

    def __init__(self, username, mail):
        assert(len(username) != 0 and "User username should not be empty")
        assert(len(mail) != 0 and "User Mail should not be empty")
        self.username = username  
        self.mail = mail


    def is_password_same(self):
        pass
        
    def validate_min_length(self, string, len_number):
        pass

    def validate_max_length(self, string, len_number):
        pass

    def already_exists(self):
        pass
