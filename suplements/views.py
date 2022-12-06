from django.shortcuts import render
from .models import *

def context_suplementos(): 
    suplementos = Suplemento.objects.all()
    context = {'suplementos': suplementos}

    return context 

def context_detalhes(id): 
    suplemento = Suplemento.objects.get(id = id)
    context = {'suplemento': suplemento}

    return context 

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def suplementos(request):
    return render(request, 'suplementos.html', context_suplementos())

def detalhes(request, id):
    return render(request, 'detalhes.html', context_detalhes(id))   







    