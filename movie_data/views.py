from django.shortcuts import render
from .models import MovieData
from rest_framework import viewsets
from .serializers import MovieSeralizer

class MovieDataView(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSeralizer

class DramaMovieDataView(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category = 'drama')
    serializer_class = MovieSeralizer

class ActionMovieDataView(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category = 'action')
    serializer_class = MovieSeralizer

class ComedyMovieDataView(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category = 'comedy')
    serializer_class = MovieSeralizer