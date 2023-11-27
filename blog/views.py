from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})
