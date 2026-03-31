from django.db import models

class Filme(models.Model):
    CATEGORIA_CHOICES = [
        ('LAN', 'Lançamento'),
        ('CLA', 'Clássico'),
        ('CUL', 'Cult'),
    ]

    titulo = models.CharField(max_length=255) # 
    diretor = models.CharField(max_length=255) # 
    ano_lancamento = models.IntegerField()
    genero = models.CharField(max_length=100)
    nota_imdb = models.FloatField()
    
    categoria = models.CharField(
        max_length=3,
        choices=CATEGORIA_CHOICES,
        default='CLA',
    )

    def __str__(self):
        return self.titulo