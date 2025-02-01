from django.shortcuts import render
from movie.models import Movie
from blog.models import Article

def home(request):
    movies = Movie.objects.all()
    articles = Article.objects.all()
    return render(request, "home.html", {"movies": movies, "articles": articles})
