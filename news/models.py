from django.db import models


class New(models.Model):
    owner = models.ForeignKey('auth.User', related_name='news')
    highlighted = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    news = models.TextField(default='')


    class Meta:
        ordering = ('created',)