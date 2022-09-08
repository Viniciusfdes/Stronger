from multiprocessing import context
from django.shortcuts import render

from .models import Suplemento

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def suplementos(request):
    suplementos = Suplemento.objects.all()
    template_name = 'suplementos.html'
    context={
        'suplementos': suplementos
    }
    return render(request, template_name, context)

def detalhes(request, id):
    suplemento = Suplemento.objects.get(id = id)
    
    template_name = 'detalhes.html'
    context = {
        'suplemento': suplemento
    }

    return render(request, template_name, context)