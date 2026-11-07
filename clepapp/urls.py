from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('focus-areas/', views.focus, name='focus'),
    path('teams/', views.teams, name='teams'),
    path('contact/', views.contact, name='contact'),
]
