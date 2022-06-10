from django.contrib import admin
from .models import Song


# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """determines how song details are displayed in the admin panel"""
    list_filter = ('playlist', 'artist')
    list_display = ('title', 'artist', 'playlist',)
    search_fields = ['title', 'artist']

    ordering = ('title',)