from django.db import models

# Create your models here.


class ScrapedWrestler(models.Model):
    
    #General Data
    wrestler_name = models.CharField(max_length=255)


    age = models.IntegerField()    
    promotion = models.CharField(max_length=255)
    active_roles = models.CharField(max_length=255)

    # Personal Data

    birth_place = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)    
    Weight = models.IntegerField()
    background_in_sports = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

    # Career Data

    alter_egos = models.CharField(max_length=255)
    roles = models.CharField(max_length=255)
    year_of_beginning = models.CharField(max_length=255)
    in_ring_experience = models.CharField(max_length=255)
    wrestling_style =  models.CharField(max_length=255)
    trainer = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    signature_moves = models.CharField(max_length=500)


    career_data = models.TextField(null=True)
    tournament_data = models.TextField(null=True)

    add_information = models.TextField(null=True)


class GameSetText(models.Model):
    game_set = models.TextField()
