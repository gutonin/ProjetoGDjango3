from django.http import HttpResponse
from django.shortcuts import render

from website.models import Post


def home_blog(request):
    lista = ['Django', 'Python', 'git']
    list_posts = Post.objects.filter(deleted=False)
    context = {
        'posts': list_posts,
        'nome': 'exibindo uma variavel nome',
        'lista_tecs': lista
    }
    return render(request, 'index.html', context)

def post_detail(request, id):
    print('salve')
    post = Post.objects.filter(id=id).first()
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)
