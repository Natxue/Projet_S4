from django.forms import ModelForm
from .models import Annonce


class AnnonceFormulaire(ModelForm):
    class Meta:
        model = Annonce
        fields = ['type', 'utilisateur', 'titre', 'details', 'prix']
