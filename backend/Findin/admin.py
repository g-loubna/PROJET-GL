from django.contrib import admin
from .models import Annonce, catégorie, théme, adresse, ExtendUser
# Register your models here.


class ExtendUseradmin(admin.ModelAdmin):
    list_display = ('r', 'address', 'phone')


class catégorieAdmin (admin.ModelAdmin):
    list_display = ('id', "nomcatégorie")


class AdresseAdmin (admin.ModelAdmin):
    list_display = ('id', 'Wilaya', 'Commune', 'adresseIMB', 'adresseURL')


class thémeAdmin (admin.ModelAdmin):
    list_display = ('id', "théme")


class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('id', "titreAnn", "catégorie", "théme", "modalité", "Description", "tarif",
                    "lieudeFormation", "photos")


admin.site.register(Annonce, AnnonceAdmin)
admin.site.register(théme, thémeAdmin)
admin.site.register(catégorie, catégorieAdmin)
admin.site.register(adresse, AdresseAdmin)
admin.site.register(ExtendUser, ExtendUseradmin)
