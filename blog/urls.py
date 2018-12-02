from django.urls import path
from . import views

urlpatterns = [
  path("<int:page>", views.articlesView),
  path("articles/<int:page>", views.articlesView, name='articles'),
  path("about/", views.aboutView),
  path("contacts/", views.contactView),
  path("post/<int:post_id>", views.postView, name='post')
]