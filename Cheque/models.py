from django.db import models

# Create your models here.
class Cheque(models.Model):
    financeira = models.CharField(max_length=100)
    nomeCliente = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    dataAbertura = models.DateField()
