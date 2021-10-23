from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:post_id>', views.post, name='post_detail'),
    path('create', views.create, name='create'),
    path('author/<int:user_id>', views.author, name='author_detail'),
    path('login', views.login, name='login'),
]
