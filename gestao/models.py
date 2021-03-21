from django.db import models

# Create your models here.
class Filmes(models.Model):
    filme = models.CharField(max_length=50)
    finalizado = models.BooleanField('Finalizado')
    resenha = models.CharField(max_length=255)
