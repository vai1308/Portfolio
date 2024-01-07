from django.contrib import admin
from django.urls import path
from Vaibhav import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html/', views.about, name='About'),
    path('contact.html/', views.contact, name='Contact'),
    path('projects.html/', views.projects, name='Projects'),
    path('thankyou.html/', views.thankyou, name='thankyou')
]
