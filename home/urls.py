from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='home'),   
    path('faqs', views.faqs, name='faqs'),
    path('bio', views.bio, name='bio'),
    path('contact', views.contact, name='contact'),
    path('repertoire', views.repertoire, name='repertoire'),
    path('services', views.services, name='services'),
    path('testimonials', views.testimonials, name='testimonials')
]
