from django.forms import ModelForm
from user.models import PrivateMessaging


class MessagingForm(ModelForm):
    class Meta:
        model = PrivateMessaging
        fields = ["title", "message"]