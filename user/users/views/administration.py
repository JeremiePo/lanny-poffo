from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .helpers.admin_pages import request_user


class Administration(TemplateView):
  
    template_name = "administration.html"
  
    def get(self, request):
        try:
        
            request_user(request.user)

        except Exception:
            return redirect("/")    
        return render(request, self.template_name)

