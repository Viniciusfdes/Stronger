from django.contrib import admin
from .models import Marca, Suplemento

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

class SuplementoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'marca', 'categoria', 'tipo', 'valor', 'imagem')

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Suplemento, SuplementoAdmin)
