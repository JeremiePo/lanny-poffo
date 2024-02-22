from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from ..forms.sign import Sign 
from .validation.validate import Validation, max_length, min_length
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .auth.Auth import Authentification
from user.models import Messaging
from django.core.mail import send_mail


def pm_admin(pseudo, mail):
    admin_username = User.objects.get(is_staff=True)
    message_to_admin = Messaging()
    message_to_admin.from_username = "Bot"
    message_to_admin.to_username = admin_username

    message_to_admin.username_to_register = pseudo
    message_to_admin.mail_to_register = mail

    message_to_admin.title = "A new user want to register"
    message_to_admin.message = "The user : " + str(pseudo) + " Want to register." + "\n" + "his mail is : " + str(mail)
    message_to_admin.save()


class SignIn(FormView):
    template_name = "sign-in.html"
    form_class = Sign
    success_url = "/login/"
    # form_class = Sign


    def get(self, request):
        return render(request, "sign-in.html", context={"form": self.form_class})


    def post(self, request):
        validation = Validation(self.request.POST["pseudo"], 
                            self.request.POST["mail"])

                            # self.request.POST["repeat_password"],
                            # 

        try:

            min_length(self.request.POST["pseudo"], 4)
            max_length(self.request.POST["pseudo"], 50)
            min_length(self.request.POST["mail"], 6)
            max_length(self.request.POST["mail"], 25)
            validation.email_already_exists()


        except ValidationError:
            message = "Sorry, someting went wrong... Can you try again?"
            return render(request, "sign-in.html", context={"form": self.form_class, "message": message})
        except IntegrityError:
            message = "Sorry, someting went wrong... Can you try again?"
            return render(request, "sign-in.html", context={"form": self.form_class, "message": message})
        
        pm_admin(self.request.POST["pseudo"], self.request.POST["mail"])
        
        return render(request, "sign-in.html")
        
        return render(request, "sign-in.html", context={"form": self.form_class, "message": message})
        """
            min_length(self.request.POST["password"], 5)
            max_length(self.request.POST["password"], 40)  
            
            validation.are_password_same()

            auth = Authentification(
                self.request.POST["pseudo"], 
                self.request.POST["password"], 
                self.request.POST["mail"]
                )
            auth.user_creation()
            admin_username = User.objects.get(is_staff=True)
            message_to_admin = Messaging()
            message_to_admin.from_username = "Bot"
            message_to_admin.to_username = admin_username
            message_to_admin.title = "A new user want to register"
            message_to_admin.message = "The user : " + str(self.request.POST["pseudo"]) + " Want to register."
            message_to_admin.save()
            
        except ValidationError:
            message = "Sorry, someting went wrong... Can you try again?"
            return render(request, "sign-in.html", context={"form": self.form_class, "message": message})
        except IntegrityError:
            message = "Sorry, someting went wrong... Can you try again?"
            return render(request, "sign-in.html", context={"form": self.form_class, "message": message})

        return redirect("/user/login/")
        """