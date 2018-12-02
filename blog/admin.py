from django.contrib import admin
from .models import Article, Commentaire

class ArticleAdmin(admin.ModelAdmin):
   list_display   = ('titre', 'auteur', 'date')
   list_filter    = ('auteur',)
   date_hierarchy = 'date'
   ordering       = ('date', )
   search_fields  = ('titre', 'contenu')

admin.site.register(Commentaire)
admin.site.register(Article, ArticleAdmin)

# Register your models here.
