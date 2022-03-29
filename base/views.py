from django.contrib.postgres.search import SearchVector, SearchQuery
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Annonce
from .forms import AnnonceFormulaire, PostSearchForm


# Create your views here.


def home(request):
    ads = Annonce.objects.all()
    context = {"annonces": ads}
    return render(request, 'base/home.html', context)


def annonce(request, pk):
    display = Annonce.objects.get(id=pk)
    if display.type == 'demande':
        ads_inverse = 'offre'
    else:
        ads_inverse = 'demande'
    # list_ads = Annonce.objects.filter(type=ads_inverse)
    list_ads = Annonce.objects.annotate(search=SearchVector(
        'titre', 'details'),).filter(search=SearchQuery(display.titre), type=ads_inverse)
    for ad in list_ads:
        if ad.prix > display.prix:
            list_ads.remove(ad)

    list_saved = display.associations.all()
    context = {'annonce': display, 'assoc': list_ads, 'saved': list_saved}
    return render(request, 'base/annonce.html', context)


def user(request):
    return render(request, 'base/user.html')


def creer_une_annonce(request):
    form = AnnonceFormulaire()
    if request.method == 'POST':
        form = AnnonceFormulaire(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/annonce_form.html', context)


def modifier_annonce(request, pk):
    annonce = Annonce.objects.get(id=pk)
    # Pré-rempli les champs ???
    form = AnnonceFormulaire(instance=annonce)

    if request.method == 'POST':
        form = AnnonceFormulaire(request.POST, instance=annonce)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/annonce_form.html', context)


def supprimer_annonce(request, pk):
    annonce = Annonce.objects.get(id=pk)
    if request.method == 'POST':
        annonce.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': annonce})


def enregistrer_annonce(request, pk, id_assoc):
    # obj = get_object_or_404(Annonce, id=pk)
    obj = Annonce.objects.get(id=pk)
    if obj.associations.filter(id=id_assoc).exists():
        obj.associations.remove(Annonce.objects.get(id=id_assoc))
    else:
        obj.associations.add(Annonce.objects.get(id=id_assoc))
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def recherche(request):
    form = PostSearchForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Annonce.objects.filter(titre__contains=q)

    context = {'form': form, 'q': q, 'results': results}
    return render(request, 'base/search.html', context)

