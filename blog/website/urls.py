from django.urls import path, include
from website.views import hello_blog

urlpatterns = [
    path('', hello_blog),
]
