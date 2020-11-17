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
        })

    context = {'articles':articlesData}
    return render(request, "index.html", context)