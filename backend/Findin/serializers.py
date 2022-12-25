from rest_framework import serializers
from .models import Annonce, adresse, théme, catégorie, ExtendUser


class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        fields = ("titreAnn", "catégorie", "théme", "modalité", "Description", "tarif",
                  "lieudeFormation", "photos")


class adresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = adresse
        fields = ('Wilaya', 'Commune', 'adresseIMB', 'adresseURL')


class thémeSerializer(serializers.ModelSerializer):
    class Meta:
        model = théme
        fields = ("théme")


class catégorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = catégorie
        fields = ("nomcatégorie")


class ExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendUser
        fields = ("r", "address", "phone")
