from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name="index" ),
    path('single-page/<int:article_id>', views.singleArticle, name="single_article")
]