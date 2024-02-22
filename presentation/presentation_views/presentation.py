from django.views.generic import TemplateView
from django.shortcuts import render, redirect


class Presentation(TemplateView):
    template_name = "index.html"
    def get(self, request):
        return render(self.request, self.template_name)

    def post(self, request):
        return render(self.request, self.template_name)    