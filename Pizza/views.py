from django.shortcuts import render
from django.http import JsonResponse
from .models import Pizza

from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response  import Response

from .serializers import PizzaSerializer


# Create your views here.
@api_view(['GET'])
def home(request):
    pizza=Pizza.objects.all()
    
    serializer=PizzaSerializer(pizza,many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def single_pizza_view(request,id):
    pizza=Pizza.objects.get(id=id)
    serializer=PizzaSerializer(pizza,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPizza(request):
    serializer=PizzaSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data)

@api_view(['POST'])
def EditPizza(request,id):
    pizza=Pizza.objects.get(id=id)
    serializer=PizzaSerializer(instance=pizza,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data)
    
@api_view(['DELETE'])
def DeletePizza(request,id):
    pizza=Pizza.objects.get(id=id)
    
    pizza.delete()
    return Response("Successfully deleted")
