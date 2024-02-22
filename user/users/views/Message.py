from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from user.models import Messaging

from django.core.mail import send_mail



def send_email_if_yes(user, mail)  -> int:

    send_mail(
    "Registration approved",
    "Your request to register on the lanny poffo website has been approved." + "\n" + "Just enter your identifiants here : " + " And register a password",
    "jeremiep842@outlook.com",
    [str(mail)],
    fail_silently=False,
)

def send_email_if_no(user, mail) -> int:
    send_mail("Registration not approved",
    "Your request to register on the lanny poffo website has not been approved by the admin",
    "jeremiep842@outlook.com",
    [str(mail)],
    fail_silently=False,
)




class Message(TemplateView):
    template_name = "message.html"


    def get(self, request, str):
        
        message_number = int(str)
        Message = Messaging.objects.get(id=message_number)


        return render(self.request, self.template_name, context={"message": Message})
    

    def post(self, request, str):
        if self.request.POST.get('yes'):
            message_number = int(str)
            Message = Messaging.objects.get(id=message_number)
            send_email_if_yes(Message.username_to_register, Message.mail_to_register)
            Message.delete()
            return redirect("/user/administration/PMessage/")

        if self.request.POST.get('no'):
            message_number = int(str)

            Message = Messaging.objects.get(id=message_number)

            send_email_if_no(Message.username_to_register, Message.mail_to_register)

            Message.delete()



            return redirect("/user/administration/PMessage/")
        
            

        return render(self.request, self.template_name)