
from django.contrib.auth.models import User

class Authentification:
    
    def __init__(self, username, password, mail):
        assert(len(username) != 0 and "Username is empty")
        assert(len(password) != 0 and "Password is empty")
        assert(len(mail) != 0 and "Mail is empty")
        self.username = username  
        self.password = password  
        self.mail = mail


    def user_creation(self):
        User.objects.create_user(self.pseudo, self.mail, self.password)