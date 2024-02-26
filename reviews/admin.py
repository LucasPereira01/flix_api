from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdimon(admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars', 'comment')
