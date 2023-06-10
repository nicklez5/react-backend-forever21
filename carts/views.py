from django.shortcuts import render
from pstats import Stats, StatsProfile
from django.http import Http404,JsonResponse
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.http import HttpResponseNotFound
from .serializers import *
from .models import *
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def carts(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CartSerializer(data)
        return Response({'Cart':serializer.data})
    elif request.method == 'POST':
        serializer = CartSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Cart':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
