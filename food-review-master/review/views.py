from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    author = request.user
    posts = Post.objects.all()
    return render(request, 'review/home.html', {'author': author,'posts': posts})

# def author(request):
#     author = request.user
#     posts = Post.objects.filter(posted_by_id=author.id)
#     return render(request, 'review/author.html', {'author': author, 'posts': posts})

def author(request, user_id):
    singleAuthor = User.objects.get(id=user_id)
    posts = Post.objects.filter(posted_by_id=user_id)
    return render(request, 'review/author.html', {'singleAuthor': singleAuthor, 'posts': posts})

def post(request, post_id):
    singlePost = Post.objects.get(id=post_id)
    return render(request, 'review/post.html', {'singlePost': singlePost})

def create(request):
    return render(request, 'review/create.html')

def login(request):
    return render(request, 'review/login.html')
