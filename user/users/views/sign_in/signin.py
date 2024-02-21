from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from ...forms.sign import Sign 
from ..ValidateForms.ValidationUser import ValidationUser
from ..ValidateForms.ValidationPassword import ValidationPassword
from ..ValidateForms.ValidationEmail import ValidationEmail
from django.core.exceptions import ValidationError



class SignIn(FormView):
    template_name = "sign-in.html"
    form_class = Sign
    success_url = "/login/"
    # form_class = Sign


    def get(self, request):
        return render(request, "sign-in.html", context={"form": self.form_class})


    def post(self, request):
        validate_user = ValidationUser(self.request.POST["pseudo"])
        validate_password = ValidationPassword(self.request.POST["password"], self.request.POST["repeat_password"])
        validate_email = ValidationEmail(self.request.POST["mail"])
        try:
            validate_user.validate_min_length()
            validate_user.validate_max_length()
            validate_user.already_exists()

            
            validate_password.is_password_same()
            validate_password.validate_min_length()
            validate_password.validate_max_length()

            validate_email.validate_max_length()
            validate_email.validate_min_length()
            validate_user.validate_max_length()

        except ValidationError:
            message = "Sorry, someting went wrong... Can you try again?"
            return render(request, "sign-in.html", context={"form": self.form_class, "message": message})
            
        User.objects.create_user(self.request.POST["pseudo"], 
                            self.request.POST["mail"],
                            self.request.POST["password"])
        return render(request, "sign-in.html", context={"form": self.form_class})

        return redirect("login")
