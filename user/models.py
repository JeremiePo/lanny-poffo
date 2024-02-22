from django.db import models

# Create your models here.


class Messaging(models.Model):
    from_username = models.CharField(max_length=50)
    to_username = models.CharField(max_length=50)
    username_to_register = models.CharField(max_length=50, null=True)
    mail_to_register = models.CharField(max_length=50, null=True)
    title = models.TextField()
    message = models.TextField()

class CanUserRegister(models.Model):
    can_register = models.BooleanField()



class PrivateMessaging(models.Model):
    from_username = models.CharField(max_length=50)
    to_username = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    date = models.DateField(null=True)
    message = models.TextField()