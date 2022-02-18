from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    comment = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.item.name
