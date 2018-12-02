from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Article, Commentaire
from .forms import CommentaireForm

def articlesView(request, page):
  articles_list = Article.objects.all()
  pages = Paginator(articles_list, 3)
  p = int(page)
  next_page = p
  previous_page = p

  if p < pages.num_pages:
   next_page = p + 1

  if p > 1:
    previous_page = p - 1 

  articles = pages.page(p).object_list

  return render(request, "blog/articles.html", locals())

def aboutView(request):
  return render(request, "blog/about.html")

def contactView(request):
  return render(request, "blog/contact.html")

def postView(request, post_id):
  article = Article.objects.get(id=post_id)  
  comForm = CommentaireForm(request.POST or None)
  commentaires = article.commentaires.all()

  if comForm.is_valid(): 
        auteur = comForm.cleaned_data['auteur']
        contenu = comForm.cleaned_data['contenu']

        commentaire = Commentaire(auteur=auteur, contenu=contenu)
        commentaire.save()

        article.commentaires.add(commentaire)
        article.save()

        envoi = True

  return render(request, "blog/post.html", locals())
