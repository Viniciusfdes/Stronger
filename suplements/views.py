from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def suplementos(request):
    return render(request, 'suplementos.html')