from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def board(request):
    articles = Article.objects.all()
    context={
        'articles': articles
    }
    return render(request, 'board.html', context)