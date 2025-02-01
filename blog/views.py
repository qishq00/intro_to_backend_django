from django.shortcuts import render

# Create your views here.
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})
