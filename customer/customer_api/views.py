from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CustomerSerializer
from .models import Customer


# Create your views here.

@api_view(['GET'])
def ShowAll(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateCustomer(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()

    return Response('Items delete successfully!')