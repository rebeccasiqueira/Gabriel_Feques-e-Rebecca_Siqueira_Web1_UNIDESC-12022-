from django.db import models

# Create your models here.
class CliAviso(models.Model):
    mensagem = models.CharField(max_length=100)
