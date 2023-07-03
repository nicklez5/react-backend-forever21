from django.shortcuts import render
from pstats import Stats, StatsProfile
from django.http import Http404,JsonResponse
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.http import HttpResponseNotFound
from .serializers import *
from .models import *
from clothes.models import *
from clothes.serializers import *
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
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_womenshirts(request,id,womenshirts_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        womenshirt = Women_Shirt.objects.get(pk=womenshirts_id)
    except Women_Shirt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.women_shirts.add(womenshirt)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.women_shirts.remove(womenshirt)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_womenshirts(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        women_shirts = data.women_shirts.all()
        serializer = WomenShirtSerializer(women_shirts,many=True)
        return Response({'WomenShirts': serializer.data})
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_womenpants(request,id,womenpants_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        womenpants = Women_Pants.objects.get(pk=womenpants_id)
    except Women_Pants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.women_pants.add(womenpants)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.women_pants.remove(womenpants)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_womenpants(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        women_pants = data.women_pants.all()
        serializer = WomenPantsSerializer(women_pants,many=True)
        return Response({'WomenPants': serializer.data})
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_womenjackets(request,id,womenjackets_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        womenjackets = Women_Jacket.objects.get(pk=womenjackets_id)
    except Women_Jacket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.women_jackets.add(womenjackets)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.women_jackets.remove(womenjackets)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_womenjackets(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method == 'GET'):
        women_jackets = data.women_jackets.all()
        serializer = WomenJacketSerializer(women_jackets,many=True)
        return Response({'WomenJackets': serializer.data})
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_womenjoggers(request,id,womenjoggers_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        womenjoggers = Women_Joggers.objects.get(pk=womenjoggers_id)
    except Women_Joggers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.women_joggers.add(womenjoggers)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.women_joggers.remove(womenjoggers)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_womenjoggers(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        women_joggers = data.women_joggers.all()
        serializer = WomenJoggersSerializer(women_joggers,many=True)
        return Response({'WomenJoggers': serializer.data})
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_necklaces(request,id,necklaces_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        necklaces = Necklace.objects.get(pk=necklaces_id)
    except Necklace.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.necklaces.add(necklaces)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.necklaces.remove(necklaces)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_necklaces(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        necklaces = data.necklaces.all()
        serializer = NecklaceSerializer(necklaces,many=True)
        return Response({'Necklaces': serializer.data})
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_glasses(request,id,glasses_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        glasses = Glasses.objects.get(pk=glasses_id)
    except Glasses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.glasses.add(glasses)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.glasses.remove(glasses)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_glasses(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        glasses = data.glasses.all()
        serializer = GlassesSerializer(glasses,many=True)
        return Response({'Glasses': serializer.data})
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_earrings(request,id,earrings_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        earring = Earring.objects.get(pk=earrings_id)
    except Earring.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.earrings.add(earring)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.earrings.remove(earring)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_earrings(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        earrings = data.earrings.all()
        serializer = EarringSerializer(earrings,many=True)
        return Response({'Earrings': serializer.data})
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_menshirts(request,id,menshirts_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        menshirt = Men_Shirt.objects.get(pk=menshirts_id)
    except Men_Shirt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.mens_shirts.add(menshirt)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.mens_shirts.remove(menshirt)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_menshirts(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        menshirts = data.mens_shirts.all()
        serializer = MenShirtSerializer(menshirts,many=True)
        return Response({'MenShirts': serializer.data})
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_menpants(request,id,menpants_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        menpants = Men_Pants.objects.get(pk=menpants_id)
    except Men_Pants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.mens_pants.add(menpants)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.mens_pants.remove(menpants)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_menpants(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        menpants = data.mens_pants.all()
        serializer = MenPantsSerializer(menpants,many=True)
        return Response({'MenPants': serializer.data})
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_menjoggers(request,id,menjoggers_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        menjoggers = Men_Joggers.objects.get(pk=menjoggers_id)
    except Men_Joggers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.mens_joggers.add(menjoggers)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.mens_joggers.remove(menjoggers)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_menjoggers(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        menjoggers = data.mens_joggers.all()
        serializer = MenJoggersSerializer(menjoggers,many=True)
        return Response({'MenJoggers' : serializer.data})
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def adc_menjackets(request,id,menjackets_id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        menjackets = Men_Jacket.objects.get(pk=menjackets_id)
    except Men_Jacket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data.mens_jackets.add(menjackets)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.mens_jackets.remove(menjackets)
        return Response(status=status.HTTP_200_OK)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_menjackets(request,id):
    try:
        data = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        menjackets = data.mens_jackets.all()
        serializer = MenJacketSerializer(menjackets,many=True)
        return Response({'MenJackets': serializer.data})
# Create your views here.
