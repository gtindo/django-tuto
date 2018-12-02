from django.db import models
from django.utils import timezone

class Commentaire(models.Model):
  auteur = models.CharField(max_length=46)
  contenu = models.TextField(max_length=250)
  date = models.DateTimeField(default=timezone.now, verbose_name="Date commentaire")

  class Meta:
    verbose_name = "commentaire"
    ordering = ['date']

  def __str__(self):
    return "commentaire "+self.auteur

class Article(models.Model):
  titre = models.CharField(max_length=100)
  auteur = models.CharField(max_length=42)
  contenu = models.TextField(null=True)
  image = models.ImageField(upload_to="static/blog/img")
  date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
  commentaires = models.ManyToManyField(Commentaire, related_name="commentaires", blank=True)

  class Meta:
    verbose_name = "article"
    ordering = ['date']

  def __str__(self):
    return self.titre




