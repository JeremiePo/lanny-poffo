from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from user.models import PrivateMessaging

class MessageTitle(TemplateView):

    template_name = "message_title.html"

    def get(self, request):
        data = PrivateMessaging.objects.filter(to_username=self.request.user).values()
        return render(self.request, self.template_name, context={"data": data})
