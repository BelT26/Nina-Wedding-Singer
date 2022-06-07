from django.shortcuts import render
from .models import Song


# Create your views here.
def index(request):
    """
    returns the home page
    """
    return render(request, 'home/index.html')


def services(request):
    """
    returns the services page
    """
    songs = Song.objects.all()
    return render(request, 'home/services.html', {
        'songs': songs})


def repertoire(request):
    """
    returns the services page
    """

    songs = Song.objects.all()
    return render(request, 'home/services.html', {
        songs: songs })

def testimonials(request):
    """
    returns the home page
    """
    return render(request, 'home/testimonials.html')


def faqs(request):
    """
    returns the home page
    """
    return render(request, 'home/faqs.html')


def contact(request):
    """
    returns the contacts page
    """
    return render(request, 'home/contact.html')


def add_song(request):
    """
    returns a form to add songs to the repertoire
    """
    return render(request, 'home/add_song.html')