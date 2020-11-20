from django.shortcuts import render, redirect
from . import models
from .forms import ContactUsForm
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404

def index(request):

    category_id = request.GET.get("category", '')

    if category_id:
        try:
            all_articles = models.Article.objects.filter(category=category_id)
        except models.Article.DoesNotExist:
            raise Http404("Category Dose Not Exist")        
    else:
        all_articles = models.Article.objects.all().order_by('-created_at')

    pages = Paginator(all_articles, 4)

    n = request.GET.get("page", 1)

    try:
        articles = pages.page(n)
    except EmptyPage:
        articles = pages.page(1)

    context = {
        'articles':articles,
        'pages_count' : range(1, pages.num_pages + 1)
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    context = {}

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid:
            my_model = form.save()
            context["show_message"] = "message send."
        else:
            context["show_message"] = "your message is not valid!"

    else :
        # form = ContactUsForm()
        context["show_message"] = ""
    
    context["form"] = ContactUsForm()
    return render(request, "contact.html", context)

def category(request):
    categories = models.Category.objects.all()
    return render(request, "category.html", {'categories':categories})

def singleArticle(request, article_id):
    article = models.Article.objects.get(id=article_id)
    context = {'article':article}
    return render(request, "singlePost.html", context)