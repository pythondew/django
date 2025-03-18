from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def my_list(request):
    posts = Post.objects.all()  # Получаем все объекты из базы
    post_list = ''  # Создаем пустую строку

    for p in posts:
        post_list += f"<li>{p.title}</li>"  # Добавляем каждый заголовок в список

    return HttpResponse(f"<ul>{post_list}</ul>") 

