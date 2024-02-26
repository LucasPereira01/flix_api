from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MovieAdimin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'genre', 'release_date', 'resume'
    )
