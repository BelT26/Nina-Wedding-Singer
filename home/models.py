from django.db import models


# Create your models here.
class Song(models.Model):
    """
    A model used to add new songs
    """
    NOUGHTIES = '00'
    NINETIES = '90'
    EIGHTIES = '80'
    SEVENTIES = '70'
    SIXTIES = '60'
    OTHER = 'OT'    
    CEREMONY = 'CE'
   
    PLAYLIST_CHOICES = [
        (NOUGHTIES, '00s - 10s'),
        (NINETIES, '90s'),
        (EIGHTIES, '80s'),
        (SEVENTIES, '70s'),
        (SIXTIES, '50s - 60s'),
        (OTHER, 'Other'), 
        (CEREMONY, 'Ceremony'),
       
    ]

    title = models.CharField(max_length=300, blank=False, null=False)
    artist = models.CharField(max_length=300, blank=False, null=False)    
    playlist = models.CharField(max_length=50, choices=PLAYLIST_CHOICES,
                                default=CEREMONY)

    def __str__(self):
        return f'{self.title}'


class Testimonial(models.Model):
    """
    A model used to add testimonials
    """
    title = models.CharField(max_length=300, blank=False, null=False)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()    
    author = models.CharField(max_length=200, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
