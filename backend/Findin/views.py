from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from .serializers import AnnonceSerializer, adresseSerializer, thémeSerializer, catégorieSerializer, ExtendSerializer
from .models import Annonce, adresse, catégorie, théme, ExtendUser


class AnnonceView(viewsets.ModelViewSet):
    serializer_class = AnnonceSerializer
    queryset = Annonce.objects.all()


class adressseView(viewsets.ModelViewSet):
    serializer_class = adresseSerializer
    queryset = adresse.objects.all()


class catégorieView(viewsets.ModelViewSet):
    serializer_class = catégorieSerializer
    queryset = catégorie.objects.all()


class thémeView(viewsets.ModelViewSet):
    serializer_class = thémeSerializer
    queryset = théme.objects.all()


class ExtenduserView(viewsets.ModelViewSet):
    serializer_class = ExtendSerializer
    queryset = ExtendUser.objects.all()
