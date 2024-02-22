from django.views.generic import TemplateView
from django.shortcuts import render
from game.models import ScrapedWrestler
from random import randint




def random_wrestler_id(request):
    latest_id = ScrapedWrestler.objects.latest("id").id
    random_id = randint(1, int(latest_id))
    print(random_id)
    return random_id



class RandomWrestler(TemplateView):

    template_name = "randomizer.html"

    def get(self, request):

        self.request.session["points"] = 3
        self.request.session["random_wrestler"] = random_wrestler_id(self.request)
        print(self.request.session["random_wrestler"])
        return render(self.request, self.template_name)

    def post(self, request):
        
        return render(self.request, self.template_name)
