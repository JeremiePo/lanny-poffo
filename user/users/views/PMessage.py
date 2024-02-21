from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from user.models import Messaging
from django.core.mail import send_mail


class PMessage(TemplateView): 
    template_name = "private_message.html"
 
    def get(self, request):
        message_number = Messaging.objects.all().values_list('id', flat=True)
        l = []
        print(self.request.GET.get("message"))
        for i in message_number:
            message = "Message Number : " + str(i)
            l.append(message)

        c = zip(l, message_number)
        # send_email()
        return render(self.request, self.template_name, context={"message" : c})