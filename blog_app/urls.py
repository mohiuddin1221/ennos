from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_view, name='services'),
    path('', views.all_view, name='team'),
    path('', views.all_view, name='temonial'),
    path('', views.all_view, name='portfolio'),
    
] 



