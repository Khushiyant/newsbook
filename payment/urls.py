from django.contrib import admin
from django.urls import path, include
from payment import views

urlpatterns = [
    path('', views.pricing, name='pricing'),
    path('checkout', views.checkout, name='checkout')

]