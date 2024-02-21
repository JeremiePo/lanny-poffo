from django.views.generic import TemplateView
from django.shortcuts import render, redirect


class Box(TemplateView):
    template_name = "box.html"