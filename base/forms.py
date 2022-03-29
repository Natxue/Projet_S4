from django.forms import ModelForm
from django import forms
from .models import Annonce


class AnnonceFormulaire(ModelForm):
    class Meta:
        model = Annonce
        fields = ['type', 'utilisateur', 'titre', 'details', 'prix']


class PostSearchForm(forms.Form):
    q = forms.CharField()
