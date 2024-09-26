from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    
# Create your models here.
