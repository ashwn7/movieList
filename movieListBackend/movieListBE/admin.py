from django.contrib import admin
from .models import movieinfo

# Register your models here.
class movielistadmin(admin.ModelAdmin):
    listDisplay = (movieinfo.movieTitle, movieinfo.synopsys, movieinfo.released, movieinfo.castAndCrew, movieinfo.genre, movieinfo.ratings)
    
admin.site.register(movieinfo, movielistadmin)