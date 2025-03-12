from django.shortcuts import render
from rest_framework import viewsets

from sports.models import Sports
from sports.serializers import SportsSerializer


# Create your views here.
class SportsViewSet(viewsets.ModelViewSet):
    queryset = Sports.objects.all()
    serializer_class = SportsSerializer