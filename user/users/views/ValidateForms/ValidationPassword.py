from .validation import Validation
from django.core.exceptions import ValidationError


class ValidationPassword(Validation):
    def __init__(self, password, repeat_password):
        super().__init__(password, repeat_password)
        assert(len(self.password, repeat_password) != 0 and "User Password should not be empty")

    def is_password_same(self):
        if self.password != self.repeat_password:
            raise ValidationError

    def validate_min_user_length(self):
        if len(self.password) < 5:
            raise ValidationError
        
    def validate_max_user_length(self):
        if len(self.password) > 40:
            raise ValidationError   