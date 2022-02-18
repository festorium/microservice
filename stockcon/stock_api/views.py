from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ItemSerializer, OrderSerializer
from .models import Item, Order


# Create your views here.

@api_view(['GET'])
def ShowAllItem(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def CreateItem(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateItem(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def createOrder(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateOrder(request, pk):
    item = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteOrder(request, pk):
    item = Order.objects.get(id=pk)
    item.delete()

    return Response('Order deleted!')
