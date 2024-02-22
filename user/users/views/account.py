from django.views.generic import TemplateView
from django.shortcuts import render

class Account(TemplateView):
  
    template_name = "account.html"
    
    

    def get(self, request):
        return render(request, self.template_name)

