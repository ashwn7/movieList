from pyexpat import model
from rest_framework import serializers
from .models import movieinfo

class movielistserializer(serializers.ModelSerializer):
    class Meta:
        model = movieinfo
        fields = ('movieTitle', 'synopsys', 'released', 'castAndCrew', 'genre', 'ratings')
    