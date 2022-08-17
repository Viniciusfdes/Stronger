from django.contrib import admin
from .models import Categoria, Marca, Suplemento

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

class SuplementoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'marca', 'categoria', 'tipo', 'valor', 'imagem')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Suplemento, SuplementoAdmin)
