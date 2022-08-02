from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .models import Song, Testimonial
from .forms import ContactForm


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
    returns the services page
    """

    songs = Song.objects.all()
    return render(request, 'home/repertoire.html', {
        'songs': songs})


def testimonials(request):
    """
    returns the home page
    """
    testimonial_list = Testimonial.objects.all()
    return render(request, 'home/testimonials.html', {
        'testimonials': testimonial_list
    })


def faqs(request):
    """
    returns the home page
    """
    return render(request, 'home/faqs.html')


def bio(request):
    """
    returns the home page
    """
    return render(request, 'home/bio.html')


def contact(request):
    """
    returns a form for the user to contact Nina
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email_address']
            subject = f"Website Inquiry from {name}"
            message = form.cleaned_data['message'],

            try:
                send_mail(subject, message, email, ['helenjtaylor26@gmail.com'])
                messages.success(request, 'Your request has been successfully submitted')
            except BadHeaderError:
                messages.error(request, 'Please check your form for errors.')
                return HttpResponse('Form error.')
            return redirect(reverse("home"))

    form = ContactForm()
    return render(request, "home/contact.html", {'form': form})

