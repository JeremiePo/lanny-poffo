
from .validation import Validation


from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class ValidationUser(Validation):

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
        

    def already_exists(self):
        if User.objects.filter(username=self.username).exists():
            raise ValidationError
