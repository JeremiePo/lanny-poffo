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




    """
    def authentification(self):
        user = authenticate(username=self.username, password=self.password, mail=self.mail)
        if user is None:
            raise Exception
        else:
            return user
        
    def already_exist(self):
        user = User.objects.get(username=self.username)
    """
class ValidateUsername(Validation):

    def __init__(self, username):
        super().__init__(username)
        assert(len(self.username) != 0 and "User username should not be empty")
    # Add max length for constructor            

    def validate_min_user_length(self):
        if len(self.username) < 4:
            raise ValidationError
        
    def validate_max_user_length(self):
        if len(self.username) > 20:
            raise ValidationError   
        
    def validate_password_length(self, string, len_number):
        if len(string) < len_number:
            raise Exception




username = ValidateUsername("username")