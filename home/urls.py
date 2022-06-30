from django.contrib import admin
from django.urls import path
from home import views
from django.urls import path, include

urlpatterns = [
    path('home/', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services')
]
