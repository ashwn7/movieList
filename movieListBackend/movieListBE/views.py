from django.shortcuts import render
from rest_framework import viewsets
from .serializers import movielistserializer
from .models import movieinfo

# Create your views here.
class movielistview(viewsets.ModelViewSet):
    serializer_class = movielistserializer
    queryset = movieinfo.objects.all()