from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Annonce(models.Model):
    # relation (1n) User_Annonce
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    # type =
    titre = models.CharField(max_length=200)
    details = models.TextField()
    prix = models.IntegerField(default=0)
    mise_en_ligne = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Message(models.Model):
    destinataire = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenu[0:50]
