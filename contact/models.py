from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)


