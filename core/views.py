from django.shortcuts import render, redirect
from .models import institutionalTeam_Contingent, Independent_Adjudicator
from .models import Cross_Open
from django import forms


def home(request):
    return render(request, 'core/HomePage.html',)

def saveContact(request):
    if request.method=="POST":
        name_Institution = request.POST.get('name_Institution')
        team_Slots = request.POST.get('team_Slots')
        adjudicator_Slots =  request.POST.get('adjudicator_Slots')
        team_rep_name = request.POST.get('team_rep_name')
        country_code = request.POST.get('country_code')
        contact_number = request.POST.get('contact_number')
        email_id_deb_soc = request.POST.get('email_id_deb_soc')
        alt_poc_name = request.POST.get('alt_poc_name')
        # alt_poc_number = request.POST.get('alt_poc_number')
        alt_poc_email_id = request.POST.get('alt_poc_email_id')
        # feedback_queries = request.POST.get('feedback_queries')
        en = institutionalTeam_Contingent(name_Institution = name_Institution, 
                                          team_Slots = team_Slots,
                                          adjudicator_Slots = adjudicator_Slots,
                                          team_rep_name = team_rep_name,
                                          contact_number = contact_number,
                                          country_code = country_code,
                                          email_id_deb_soc = email_id_deb_soc,
                                          alt_poc_name = alt_poc_name,
                                        #   alt_poc_number = alt_poc_number,
                                          alt_poc_email_id = alt_poc_email_id)
                                        #   feedback_queries = feedback_queries)
        en.save()
        return render(request, "core/HomePage.html")
    else:
        return render(request, "core/HomePage.html", {'forms': en})
    
def saveContact2(request):
    if request.method=="POST":
        name_Team = request.POST.get('name_Team')
        team_leader_name = request.POST.get('team_leader_name')
        adjudicator_Slots =  request.POST.get('adjudicator_Slots')
        country_code = request.POST.get('country_code')
        contact_number = request.POST.get('contact_number')
        email_id_head = request.POST.get('email_id_head')
        alt_poc_name = request.POST.get('alt_poc_name')
        alt_country_code = request.POST.get('alt_country_code')
        alt_poc_number = request.POST.get('alt_poc_number')
        alt_poc_email_id = request.POST.get('alt_poc_email_id')
        # feedback_queries = request.POST.get('feedback_queries')
        en = Cross_Open(name_Team = name_Team, 
                        team_leader_name = team_leader_name,
                        adjudicator_Slots = adjudicator_Slots,
                        contact_number = contact_number,
                        country_code = country_code,
                        email_id_head = email_id_head,
                        alt_poc_name = alt_poc_name,
                        alt_poc_number = alt_poc_number,
                        alt_country_code = alt_country_code,
                        alt_poc_email_id = alt_poc_email_id)
                        # feedback_queries = feedback_queries)
        en.save()
        return render(request, "core/HomePage.html")
    else: 
        return render(request, "core/HomePage.html", {'forms': en})
    
def saveContact3(request):
    if request.method=="POST":
        name_adjud = request.POST.get('name_adjud')
        institution_name = request.POST.get('institution_name')
        country_code = request.POST.get('country_code')
        contact_number =  request.POST.get('contact_number')
        email_id_head = request.POST.get('email_id_head')
        alt_country_code = request.POST.get('alt_country_code')
        alt_poc_number = request.POST.get('alt_poc_number')
        alt_poc_email_id = request.POST.get('alt_poc_email_id')
        # feedback_queries = request.POST.get('feedback_queries')
        en = Independent_Adjudicator(name_adjud = name_adjud, 
                        institution_name = institution_name,
                        contact_number = contact_number,
                        country_code = country_code,
                        email_id_head = email_id_head,
                        alt_poc_number = alt_poc_number,
                        alt_country_code = alt_country_code,
                        alt_poc_email_id = alt_poc_email_id)
                        # feedback_queries = feedback_queries)
        en.save()
        return render(request, "core/HomePage.html")
    else: 
        return render(request, "core/HomePage.html", {'forms': en})


def instTeam(request):
    return render(request, 'core/instituteTeamCont.html',)

def CrossOpen(request):
    return render(request, 'core/crossOpen.html',)

def indAdjudicator(request):
    return render(request, 'core/independentAdjudicator.html',)

# def register1(request):
#     if request.method == 'POST':
#         form = institutionalTeam_Contingent(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('HomePage')
#     else:
#         form = institutionalTeam_Contingent()
#     return render(request, 'saveContact', {'form' : form})

# def register2(request):
#     if request.method == 'POST':
#         form = Cross_Open(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('HomePage')
#     else:
#         form = Cross_Open()
#     return render(request, 'saveContact2', {'form' : form})

# def register3(request):
#     if request.method == 'POST':
#         form = Independent_Adjudicator(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('HomePage')
#     else:
#         form = Independent_Adjudicator()
#     return render(request, 'saveContact3')
    
