from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status 
from .serializers import SerializeProfile
from .models import Profile
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def Profiles(request,id):
    try:
        data = Profile.objects.get(pk=id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SerializeProfile(data)
        return Response({'Profile': serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = SerializeProfile(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Profile':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
