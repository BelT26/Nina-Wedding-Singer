from django.contrib import admin
from .models import Song, Testimonial


# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """determines how song details are displayed in the admin panel"""
    list_filter = ('playlist', 'artist')
    list_display = ('title', 'artist', 'playlist',)
    search_fields = ['title', 'artist']

    ordering = ('title',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """determines how testimonials are displayed in the admin panel"""
    list_display = ('author', 'date')

    ordering = ('date',)
