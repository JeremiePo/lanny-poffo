from .validation import Validation
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class ValidationEmail(Validation):
    def __init__(self, email):
        super().__init__(email)
        assert(len(self.email) != 0 and "User Email should not be empty")
    # Add max length for constructor            

    def validate_min_user_length(self):
        if len(self.email) < 5:
            raise ValidationError
        
    def validate_max_user_length(self):
        if len(self.email) > 50:
            raise ValidationError   
    
    def already_exists(self):
        if User.objects.filter(email=self.email).exists():
            raise ValidationError
    
