from django.db import models


class cliente(models.Model):
    login = models.CharField(max_length=15)
    senha = models.CharField(max_length=15)
    data_nascimento = models.CharField(max_length=30)
    