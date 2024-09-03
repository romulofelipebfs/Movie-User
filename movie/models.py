from typing import Iterable
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField(null=True)
    genero = models.CharField(max_length=20)
    diretor = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, db_index=True, blank=True)
    favoritado_por = models.ManyToManyField(User, related_name='filmes_favoritos', blank=True)

    def __str__(self):
        return f"{self.titulo}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super(Filme, self).save(*args, **kwargs)

  