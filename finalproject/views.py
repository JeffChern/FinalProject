from django.shortcuts import render
from datetime import datetime
from .models import Article

def index(request):
    context = {
        'current_date':datetime.now(),
        'title':'Home'
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'current_date':datetime.now(),
        'title':'About'
    }
    return render(request, 'about.html', context)

def image(request):
    populate_db()
    articles = get_articles()

    context = {
        'articles':articles,
        'current_date':datetime.now(),
        'title':'Image'
    }
    return render(request, 'image.html', context)

def get_articles():
    result = Article.objects.all()
    return result

def populate_db():
    if Article.objects.count() == 0:
        Article(title = 'first image', content = 'this is the first db image').save()
        Article(title = 'second image', content = 'this is the second db image').save()
        Article(title = 'third image', content = 'this is the third db image').save()