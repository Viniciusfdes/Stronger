from ast import mod
from contextlib import nullcontext
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=40)
    
    def __str__(self):
       return self.nome 

class Marca(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
       return self.nome 

    
class Suplemento(models.Model): 

    TIPO_CHOICES = (
        ('hip', 'Hipercalórico'),
        ('ter', 'Termogênico'),
        ('pro', 'Proteico'),
        ('antx', 'Antioxidante'),
        ('horm', 'Hormonal'),
        ('vit', 'Polivitamínico'),
        ('pbc', 'Probiótico'),
        ('amn', 'Aminoácido')
    )
   
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=4, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='suplementos/', blank=True, null=True, max_length=250)

    def __str__(self):
        return self.nome 



