from unicodedata import name
from django.urls import path
from website.views import home_blog, post_detail

urlpatterns = [
    path('', home_blog, name='home_blog'),
    path('post/<int:id>/', post_detail, name='post_detail')
]
