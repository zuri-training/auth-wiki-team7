from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('documentation/', views.documentation, name='documentation'),
    path('terms/', views.terms, name='terms'),
    path('team/', views.team, name='team'),
    path('reference/', views.reference, name='reference'),
    path('faqs/', views.faqs, name='faqs'),

]

