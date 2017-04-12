from django.db import models


class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)

    class Meta:
        ordering = ('created',)
