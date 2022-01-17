from django.db import models

# Create your models here.

class movieinfo(models.Model):
    movieTitle = models.CharField(max_length=75)
    synopsys = models.TextField(max_length=300)
    released = models.BooleanField(default=True)
    castAndCrew = models.TextField(max_length=200)
    genre = models.CharField(max_length=30)
    ratings = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.movieTitle
