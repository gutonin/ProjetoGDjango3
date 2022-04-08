from django.http import HttpResponse
from django.shortcuts import render

from website.models import Post


def hello_blog(request):
    lista = ['Django', 'Python', 'git']
    list_posts = Post.objects.all()
    context = {
        'posts': list_posts,
        'nome': 'exibindo uma variavel nome',
        'lista_tecs': lista
    }
    return render(request, 'index.html', context)
