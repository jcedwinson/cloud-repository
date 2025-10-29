from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "genre", "release_year", "rating")
    search_fields = ("name", "actor", "actress")
    list_filter = ("genre", "release_year")
