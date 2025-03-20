from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, CommentForm, PostForm
from django.contrib.auth.decorators import login_required

def index(request):
    posts = Post.objects.all()
    data = {
        'title': 'Главная странциа',
        'posts': posts
    }
    return render(request, 'cp/index.html', context=data)

def post(request, post_id):
    post_inf = get_object_or_404(Post, id=post_id)
    comments = post_inf.comments.all()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  
            comment.number_post = post_inf
            comment.save()
            return redirect('post', post_id=post_id)
    else:
        form = CommentForm()

    data = {
        'title': f'Пост №{post_id}',
        'post': post_inf,
        'comments': comments,
        'form': form
    }
    return render(request, 'cp/post.html', context=data)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'cp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'cp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')  
    else:
        form = PostForm()

    return render(request, 'cp/create_post.html', {'form': form})

def search_posts(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Post.objects.filter(text__icontains=query) 

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'cp/search_results.html', context)
