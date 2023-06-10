from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView 
from .serializers import UserSerializer,RegisterSerializer,UserLoginSerializer,UserChangePasswordSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from auth import settings
import jwt, datetime
@api_view(['GET'])
@permission_classes([IsAdminUser])
def user_list(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        register_serializer = RegisterSerializer(data=request.data)
        tokens = {}
        if register_serializer.is_valid():
            CustomUser = register_serializer.save()
            refresh = RefreshToken.for_user(CustomUser)
            tokens = {
                'refresh' : str(refresh),
                'access' : str(refresh.access_token)
            }
            return Response(tokens,status=status.HTTP_201_CREATED)
        return Response(register_serializer,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def user_view(request):
    if request.method == 'POST':
        serializer_class = UserLoginSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        user = serializer_class.validated_data['user']
        return Response({
            'user_id': user.pk,
            'email': user.email
        })
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def users(request,id):
    try:
        custom_user = User.objects.get(pk=id)
    except custom_user.DoesNotExist:
        raise status.HTTP_404_NOT_FOUND
    if request.method == 'GET':
        serializer = UserSerializer(custom_user)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        custom_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_password(request,id):
    try:
        custom_user = User.objects.get(pk=id)
    except custom_user.DoesNotExist:
        raise status.HTTP_404_NOT_FOUND
    serializer = UserChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        old_password = serializer.data.get("old_password")
        if not custom_user.check_password(old_password):
            return Response({"old_password" : {"Wrong password."}},
                            status=status.HTTP_400_BAD_REQUEST)
        custom_user.set_password(serializer.data.get("new_password"))
        custom_user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
