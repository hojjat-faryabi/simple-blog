from django.shortcuts import render
from . import models

def index(request):

    articlesData = []
    articles = models.Article.objects.all().order_by('-created_at')[:4]

    for article in articles:
        articlesData.append({
            'title' : article.title,
            'description' : article.description,
            'category' : article.category,
            'id' : article.id
        })

    context = {'articles':articlesData}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def singleArticle(request, article_id):
    article = models.Article.objects.get(id=article_id)
    context = {'article':article}
    return render(request, "singlePost.html", context)