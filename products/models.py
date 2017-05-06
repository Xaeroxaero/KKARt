from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField


malowanie = [(1, 'akryl'), (2, 'olejna'), (3, 'akwarela')]


class Product(models.Model):

    owner = models.ForeignKey('auth.User', related_name='products')
    highlighted = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    image_source = VersatileImageField('Image_source', upload_to='products/images/', ppoi_field='image_source_ppoi',
                                       default='')
    about = models.TextField(default='')
    metod = models.CharField(max_length=100, default='', blank=True)
    price = models.CharField(max_length=100, default='', blank=True)
    painting_size = models.CharField(max_length=100, default='', blank=True)

    image_source_ppoi = PPOIField()



    class Meta:
        ordering = ('created',)