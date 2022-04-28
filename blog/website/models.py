from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.utils.translation import gettext as _


class Categorias(models.TextChoices):
    TECH = 'TC', _('Tecnologia')
    CR = 'CR', _('Curiosidades')
    GR = 'GR', _('Geral')


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    text = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    deleted = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title

    full_name.admin_order_field = 'title'

    def get_category_label(self):
        return self.get_category_display()

