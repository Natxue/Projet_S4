from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('annonce/<str:pk>', views.annonce, name="annonce"),
    path('user/', views.user, name="user"),

    path('nouvelle-annonce/', views.creer_une_annonce, name="nouvelle-annonce"),
    path('modifier-annonce/<str:pk>', views.modifier_annonce, name="modifier-annonce"),
    path('supprimer-annonce/<str:pk>', views.supprimer_annonce, name="supprimer-annonce"),
    path('enregistrer-annonce/<str:pk>/<str:id_assoc>', views.enregistrer_annonce, name="enregistrer-annonce"),

]