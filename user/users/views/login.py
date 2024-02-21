from django.views.generic.edit import FormView
from ..forms.log import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .helpers.validate import Validation
from user.models import Messaging

class Login(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "my-account"

    def get(self,  request):
        return render(request, "login.html", context={"form": self.form_class})

    def post(self, request):



        user = authenticate(username=self.request.POST["pseudo"], password=self.request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect("account")
          
        else:
            message = "Sorry, someting went wrong... Can you try again?"
            return render(request, "login.html", context={"form": self.form_class, "message": message})
        



        #return render(request, "account")
