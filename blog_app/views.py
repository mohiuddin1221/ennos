from typing import Any
from django import forms
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import (
    services,
    Team,
    Testimonials,
)
from .forms import(
    contactform
)

# Create your views here.

def all_view(request):
    services_obj = services.objects.all()
    team_obj = Team.objects.all()
    testimonials_obj = Testimonials.objects.all()
    contact_form = contactform()
    
    if request.method == "POST":
        contact_form = contactform(request.POST)
        if contact_form.is_valid():
            contact_form.save()
    context = {
        'services_obj' : services_obj,
        'team_obj' : team_obj,
        'testimonials_obj': testimonials_obj,
        'contact_form':contact_form  ,
        'sections': ['services_obj', 'team_obj', 'testimonials_obj','contact_form']  
    }
    
        
    return render(request,'index.html',context)



    

    
    

