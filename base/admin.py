from django.contrib import admin

# Register your models here.

from .models import Annonce, Message

admin.site.register(Annonce)
admin.site.register(Message)
