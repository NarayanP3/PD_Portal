from django.db import models
from django.core.validators import (MinValueValidator)
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django import forms


class User(AbstractUser):
    phone_number = PhoneNumberField();

class institutionalTeam_Contingent(models.Model):
    name_Institution = models.CharField(max_length = 255)
    team_Slots = models.IntegerField()
    adjudicator_Slots =  models.IntegerField()
    team_rep_name = models.CharField(max_length = 255)
    country_code = models.CharField(max_length=5)
    contact_number = PhoneNumberField()
    email_id_deb_soc = models.EmailField(max_length = 255)
    alt_poc_name = models.CharField(max_length = 255)
    # alt_poc_number = PhoneNumberField()
    alt_poc_email_id = models.EmailField(max_length = 255)
    # feedback_queries = models.CharField(max_length = 500, null=True, blank=True)
    def __str__(self):
        return '%s' % (self.name_Institution)       

class Cross_Open(models.Model):
    name_Team = models.CharField(max_length = 255)
    team_leader_name = models.CharField(max_length = 255)
    adjudicator_Slots =  models.IntegerField()
    country_code = models.CharField(max_length=5, null=True, blank=True)
    contact_number = PhoneNumberField()
    email_id_head = models.EmailField(max_length = 255, null=True, blank=True)
    alt_poc_name = models.CharField(max_length = 255)
    alt_country_code = models.CharField(max_length=5, null=True, blank=True)
    alt_poc_number = PhoneNumberField()
    alt_poc_email_id = models.EmailField(max_length = 255)
    # feedback_queries = models.CharField(max_length = 500, null=True, blank=True)
    def __str__(self):
        return '%s' % (self.name_Team)

class Independent_Adjudicator(models.Model):
    name_adjud = models.CharField(max_length = 255)
    institution_name = models.CharField(max_length = 255)
    country_code = models.CharField(max_length=5, null=True, blank=True)
    contact_number = PhoneNumberField()
    email_id_head = models.EmailField(max_length = 255)
    alt_country_code = models.CharField(max_length=5, null=True, blank=True)
    alt_poc_number = PhoneNumberField()
    alt_poc_email_id = models.EmailField(max_length = 255)
    # feedback_queries = models.CharField(max_length = 500)
    def __str__(self):
        return '%s' % (self.name_adjud)
    

# class Competition(models.Model):
#     Name = models.CharField(max_length = 255=255)
#     city_name = models.CharField(max_length = 255=255,default="None")
#     min_participant = models.IntegerField(validators=[MinValueValidator(1)])
#     max_participant = models.IntegerField(validators= [MinValueValidator(1)])
#     Details = models.TextField()
#     is_Solo = models.BooleanField(default=True)
#     guidelines=models.CharField(max_length = 255=500)
#     def __str__(self):
#         return self.Name

# # def validate_max_participant(value):
# #     min_participant = Competition.objects.first().min_participant
# #     if value < min_participant:
# #         raise ValidationError('Max participants must be greater than or equal to min participants.')
        
# class Heads_data(models.Model):
#     city= models.ForeignKey('City', on_delete=models.CASCADE, null=True)
#     competition = models.ForeignKey('Competition', on_delete=models.CASCADE, related_name='team_leaders')
#     Number_of_Participants = models.IntegerField()
#     GENDER = (
#         ('female','female'),
#         ('male','male'),
#         ('others','others')
#     )

#     # mem_no = models.IntegerField(validators=[MinValueValidator(0)])

#     team_name = models.CharField(max_length = 255=255)
#     team_heads_name = models.CharField(max_length = 255=255)
#     heads_gender = models.CharField( max_length = 255=6,choices=GENDER)
#     heads_contact_number  = models.CharField(max_length = 255 = 10)
#     heads_email = models.EmailField( max_length = 255=254)
#     heads_program_enrolled = models.CharField(max_length = 255=255)
#     heads_institute_name = models.CharField(max_length = 255=255)
#     heads_year_of_passing = models.CharField(max_length = 255 = 4)

#     def __str__(self):
#         return self.team_heads_name



# class Members_data(models.Model):
#     city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
#     competition = models.ForeignKey('Competition', on_delete=models.CASCADE)
#     team_leader = models.ForeignKey('Heads_data', on_delete=models.CASCADE)
#     GENDER = (
#         ('female','Female'),
#         ('male','Male'),
#         ('others','Others')
#     )

#     members_name = models.CharField(max_length = 255=255)
#     gender = models.CharField( max_length = 255=6,choices=GENDER)
#     members_contact_number = models.CharField(max_length = 255 = 10)
#     email = models.EmailField(max_length = 255=254)
#     program_enrolled = models.CharField(max_length = 255=255)
#     institute_name = models.CharField(max_length = 255=255)
#     year_of_passing = models.CharField(max_length = 255 = 4)

#     # Member = models.CharField(max_length = 255=255)
    
#     def __str__(self):
#         return self.members_name
