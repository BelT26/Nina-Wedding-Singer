from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='home'),
    path('add_song', views.add_song, name='add_song'),
    path('faqs', views.faqs, name='faqs'),
    path('contact', views.contact, name='contact'),
    path('repertoire', views.repertoire, name='repertoire'),
    path('services', views.services, name='services'),
    path('testimonials', views.testimonials, name='testimonials')
]
