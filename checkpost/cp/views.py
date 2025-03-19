from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    data = {
        'title': 'Главная странциа',
        'posts': posts
    }
    return render(request, 'cp/index.html', context=data)

def post(request, post_id):
    return HttpResponse("пост")
