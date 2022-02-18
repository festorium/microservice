from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=200)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name