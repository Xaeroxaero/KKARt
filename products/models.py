from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import cloudinary
import cloudinary.uploader
import cloudinary.api

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
malowanie = [(1, 'akryl'), (2, 'olejna'), (3, 'akwarela')]

class Product(models.Model):
    owner = models.ForeignKey('auth.User', related_name='products')
    highlighted = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    image_source = models.ImageField(upload_to='images/')
    metod = models.CharField(choices=malowanie, default='', max_length=100)
    price = models.CharField(max_length=100, default='', blank=True)





    class Meta:
        ordering = ('created',)
# Create your models here.


class New(models.Model):
    owner = models.ForeignKey('auth.User', related_name='news')
    highlighted = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    news = models.TextField(default='')


    class Meta:
        ordering = ('created',)