from django.db import models


class ModelContas(models.Models):
    name = models.CharField(max_length=100, verbose_name='Nome')
    
