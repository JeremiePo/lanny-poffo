from .auth.Auth import Authentification
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from ..forms.register import RegisterForm
from django.shortcuts import render
from user.models import Messaging


def request_messaging(request) -> bool:
    pseudo = request.POST["pseudo"]
    mail = request.POST["mail"]
    password = request.POST["password"]
    repeat_password = request.POST["repeat_password"]
    get_pseudo = Messaging.objects.filter(username_to_register=str(pseudo)).values()
    get_mail = Messaging.objects.filter(mail_to_register=str(mail)).values()

    if len(get_pseudo) > 0 and len(get_mail) > 0:
        return True
    
    return False



def verify_same_password(password_one, password_two) -> bool:
    if str(password_one) == str(password_two):
        return True
    return False


def password_length(password_one) -> bool:
    if len(password_one) > 4:
        return True 
    return False

def register_user(request) -> None:
    user = User.objects.create_user(str(request.POST["pseudo"]), str(request.POST["mail"]), request.POST["password"])
    user.save()
class Register(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = ""

    def get(self, request):

        register_form = RegisterForm()

        return render(self.request, self.template_name, context={"register_form": register_form})
    def post(self, request):

        register_form = RegisterForm(self.request.POST)
        if register_form.is_valid():
            if request_messaging(self.request) and verify_same_password(self.request.POST["password"], self.request.POST["repeat_password"]) and password_length(self.request.POST["password"]):
                register_user(self.request)

        messaging = Messaging()

        return render(self.request, self.template_name, context={"register_form": register_form})