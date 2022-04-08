from urllib import response
from django.http import HttpResponse
from django.utils.translation import gettext as _


def hello_world(request):
    print(_('Teste de Tradução'))
    return HttpResponse('foi')

# def hello_world(request):
#     context = {
#         'ola': 'ola!'
#     }
#     return render(request, 'index.html', context)