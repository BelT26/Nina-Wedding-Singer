from django.shortcuts import render


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
    return render(request, 'home/services.html')


def repertoire(request):
    """
    returns the repertoire page
    """
    return render(request, 'home/repertoire.html')


def testimonials(request):
    """
    returns the home page
    """
    return render(request, 'home/testimonials.html')


def bio(request):
    """
    returns the home page
    """
    return render(request, 'home/bio.html')


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