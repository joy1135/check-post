from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'cp/index.html')

def post(request, post_id):
    return HttpResponse("пост")
