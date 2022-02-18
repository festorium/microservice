from rest_framework import serializers
from .models import Item, Order


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'price', 'description')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('item', 'quantity', 'comment')
