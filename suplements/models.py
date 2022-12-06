from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
       return self.nome 

class Suplemento(models.Model): 
    
    TIPO_CHOICES = (
        ('cab', 'Carboidratos'),
        ('ter', 'Termogênico'),
        ('pro', 'Proteico'),
        ('antx', 'Antioxidante'),
        ('horm', 'Hormonal'),
        ('vit', 'Polivitamínico'),
        ('pbc', 'Probiótico'),
        ('amn', 'Aminoácido')
    )

    CATEGORIA_CHOICES = (
        ('ter', 'Termogênico'),
        ('wey', 'WheyProtein'),
        ('col', 'Colágeno'),
        ('alb', 'Albumina'),
        ('car', 'Carnitina'),
        ('mvit', 'Multivitamínico'),
        ('bcaa', 'BCAA'),
        ('glu', 'Glutamina'),
        ('cre', 'Creatina'),
        ('arg', 'Arginina'),
        ('Hip', 'Hipercalórico')
    )
   
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=4, choices=CATEGORIA_CHOICES)
    tipo = models.CharField(max_length=4, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='suplementos/', blank=True, null=True, max_length=250)

    def __str__(self):
        return self.nome 



