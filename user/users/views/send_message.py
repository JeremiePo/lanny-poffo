from django.views.generic import TemplateView
from ..forms.form_list_user import MessagingForm
from user.models import PrivateMessaging
from datetime import datetime
from django.shortcuts import render


class SendMessage(TemplateView):
    
    template_name = "send_message.html"

    def submit_data(self, request, title, message):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        private_messaging = PrivateMessaging()
        private_messaging.from_username = request.user
        private_messaging.to_username = request.session.get('to_username')
        private_messaging.date = now
        private_messaging.title = title
        private_messaging.save()



    def get(self, request):
        form = MessagingForm()
        return render(self.request, self.template_name, context={"form": form})

    def post(self, reuqest):
        form = MessagingForm(self.request.POST)
        if form.is_valid():
            self.submit_data(self.request, self.request.POST.get("title"), self.request.POST.get("message"))
        return render(self.request, self.template_name)
