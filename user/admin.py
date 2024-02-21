from django.contrib import admin
from .models import Messaging, PrivateMessaging
# Register your models here.

admin.site.register(Messaging)

admin.site.register(PrivateMessaging)