from django.contrib import admin
from django.urls import path, include
from landing import views

urlpatterns = [
    path('', views.landingPage, name='landing')
]
