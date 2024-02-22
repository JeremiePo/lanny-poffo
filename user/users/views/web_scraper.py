from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .helpers.admin_pages import request_user
from .scrape import main_function
from .present_data import ScrapedWrestlerData, GeneralScrapedData, CareerScrapedData, PersonnalScrapedData, CareerListScrapedData, TournamentsListScrapedData
from game.models import ScrapedWrestler


# from user.models import *

def store_data() -> bool:



    career_list = []
    tournament_list = []
    l = (main_function(career_list, tournament_list))
    
    general_scraped_data = GeneralScrapedData(l) 
    general_scraped_data.parse_list_scraped_data()
    personnal_scraped_data = PersonnalScrapedData(l) 
    personnal_scraped_data.parse_list_scraped_data()
    career_scraped_data = CareerScrapedData(l) 
    career_scraped_data.parse_list_scraped_data()

    scraped_wrestler = ScrapedWrestler(l)
    

    career_list_scraped_data = CareerListScrapedData(career_list)

    career_list_scraped_data.parse_list_scraped_data()

    tournaments_list_scraped_data = TournamentsListScrapedData(tournament_list)

    tournaments_list_scraped_data.parse_list_scraped_data()
    scraped_wrestler.wrestler_name = general_scraped_data.wrestler_name
    
    for row in ScrapedWrestler.objects.all().reverse():
        if ScrapedWrestler.objects.filter(wrestler_name=row.wrestler_name).count() > 1:            
            row.delete()
    
    exist_wrestler = ScrapedWrestler.objects.filter(wrestler_name=scraped_wrestler.wrestler_name).count()
    
    if exist_wrestler == 0:
        id = ScrapedWrestler.objects.all().values('id')
        if str(id) == "<QuerySet []>":
            scraped_wrestler.id = 1
        else:
            latest_id = ScrapedWrestler.objects.latest('id').id
            scraped_wrestler.id = latest_id + 1
   
    

        if scraped_wrestler.age != '':
            scraped_wrestler.age = general_scraped_data.age
        scraped_wrestler.promotion = general_scraped_data.promotion
        scraped_wrestler.active_roles = general_scraped_data.active_roles

        scraped_wrestler.birth_place = personnal_scraped_data.birth_place
        scraped_wrestler.gender = personnal_scraped_data.gender
        scraped_wrestler.Weight = personnal_scraped_data.weight
        scraped_wrestler.background_in_sports = personnal_scraped_data.background_in_sports
        scraped_wrestler.website = personnal_scraped_data.website
            
        scraped_wrestler.alter_egos = career_scraped_data.alter_egos
        scraped_wrestler.roles = career_scraped_data.roles
        scraped_wrestler.year_of_beginning = career_scraped_data.year_of_beginning
        scraped_wrestler.in_ring_experience = career_scraped_data.in_ring_experience
        scraped_wrestler.wrestling_style = career_scraped_data.wrestling_style
        scraped_wrestler.trainer = career_scraped_data.trainer
        scraped_wrestler.nickname = career_scraped_data.nickname
        scraped_wrestler.signature_moves = career_scraped_data.signature_moves
        
        scraped_wrestler.career_data = career_list_scraped_data.career_list_field
        scraped_wrestler.tournament_data = tournaments_list_scraped_data.tournaments_field
        
        scraped_wrestler.save()
        return True
    else:
        return False


class WebScraper(TemplateView):
  
    template_name = "web_scraper.html"
  
    def get(self, request):
                

        return render(request, self.template_name)


    def post(self, request):
        data = ""
        counter = 0
        try:
            store = store_data()
            if store:
                data = "Data scraped Succesfuly!"
            else:
                while counter < 5 and store != True:
                    counter += 1
                    store = store_data()
                    print(counter)
                data = "This Wrestler already exists... Try adjusting the parameters."

        except ValueError:
            pass
        
        return render(request, self.template_name, context={"data": data})