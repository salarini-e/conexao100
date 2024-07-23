from django.contrib import admin
from .models import Preinscricao
from .forms import PreinscricaoForm

class PreinscricaoAdmin(admin.ModelAdmin):
    form = PreinscricaoForm
    list_display = ('nome', 'email', 'whatsapp', 'genero', 'idade', 'ocupacao')
    search_fields = ('nome', 'email', 'whatsapp')
    list_filter = ('genero', 'ocupacao')

admin.site.register(Preinscricao, PreinscricaoAdmin)