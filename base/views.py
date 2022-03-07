from django.shortcuts import render, redirect
from .models import Annonce
from .forms import AnnonceFormulaire

# Create your views here.


def home(request):
    ads = Annonce.objects.all()
    context = {"annonces": ads}
    return render(request, 'base/home.html', context)


def annonce(request, pk):
    display = Annonce.objects.get(id=pk)
    context = {'annonce': display}
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

