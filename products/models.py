from django.db import models



malowanie = [(1, 'akryl'), (2, 'olejna'), (3, 'akwarela')]

class Product(models.Model):
    owner = models.ForeignKey('auth.User', related_name='products')
    highlighted = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    image_source = models.ImageField(upload_to='products/images/')
    metod = models.CharField(choices=malowanie, default='', max_length=100)
    price = models.CharField(max_length=100, default='', blank=True)





    class Meta:
        ordering = ('created',)