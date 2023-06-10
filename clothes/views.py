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
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def MenShirts(request):
    if request.method == 'GET':
        shirts = Men_Shirt.objects.all()
        serializer = MenShirtSerializer(shirts,many=True)
        return Response({'MenShirts': serializer.data})
    elif request.method == 'POST':
        serializer = MenShirtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MenShirts': serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def MenShirt(request,id):
    try:
        data = Men_Shirt.objects.get(pk=id)
    except Men_Shirt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MenShirtSerializer(data)
        return Response({'MenShirt': serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = MenShirtSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MenShirt':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def MenJackets(request):
    if request.method == 'GET':
        jackets = Men_Jacket.objects.all()
        serializer = MenJacketSerializer(jackets,many=True)
        return Response({'MenJackets': serializer.data})
    elif request.method == 'POST':
        serializer = MenJacketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MenJackets':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def MenJacket(request,id):
    try:
        data = Men_Jacket.objects.get(pk=id)
    except Men_Jacket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MenJacketSerializer(data)
        return Response({'MenJacket':serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = MenJacketSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MenJacket':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def MenPants(request):
    if request.method == 'GET':
        pants = Men_Pants.objects.all()
        serializer = MenPantsSerializer(pants,many=True)
        return Response({'MenPants': serializer.data})
    elif request.method == 'POST':
        serializer = MenPantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MenPants':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def MenPant(request,id):
    try:
        data = Men_Pants.objects.get(pk=id)
    except Men_Pants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MenPantsSerializer(data)
        return Response({'MenPant':serializer.data})
    elif request.method == 'POST':
        serializer = MenPantsSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MenPant':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def MenJoggers(request):
    if request.method == 'GET':
        joggers = Men_Joggers.objects.all()
        serializer = MenJoggersSerializer(joggers,many=True)
        return Response({'MenJoggers': serializer.data})
    elif request.method == 'POST':
        serializer = MenJoggersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MenJoggers':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def MenJogger(request,id):
    try:
        data = Men_Joggers.objects.get(pk=id)
    except Men_Joggers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MenJoggersSerializer(data)
        return Response({'MenJogger':serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = MenJoggersSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MenJogger':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def glasses(request):
    if request.method == 'GET':
        glasses = Glasses.objects.all()
        serializer = GlassesSerializer(glasses,many=True)
        return Response({'Glasses': serializer.data})
    elif request.method == 'POST':
        serializer = GlassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Glasses':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def glass(request,id):
    try:
        data = Glasses.objects.get(pk=id)
    except Glasses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GlassesSerializer(data)
        return Response({'Glass':serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = GlassesSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Glass':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def earrings(request):
    if request.method == 'GET':
        earrings = Earring.objects.all()
        serializer = EarringSerializer(earrings,many=True)
        return Response({'Earrings': serializer.data})
    elif request.method == 'POST':
        serializer = EarringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Earrings':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def earring(request,id):
    try:
        data = Earring.objects.get(pk=id)
    except Earring.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EarringSerializer(data)
        return Response({'Earring': serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = EarringSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Earring':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def necklaces(request):
    if request.method == 'GET':
        necklaces = Necklace.objects.all()
        serializer = NecklaceSerializer(necklaces,many=True)
        return Response({'Necklaces': serializer.data})
    elif request.method == 'POST':
        serializer = NecklaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Necklaces':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','DELETE','POST'])
@permission_classes([IsAuthenticated])
def necklace(request,id):
    try:
        data = Necklace.objects.get(pk=id)
    except Necklace.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NecklaceSerializer(data)
        return Response({'Necklace':serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = NecklaceSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Necklace':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def WomenShirts(request):
    if request.method == 'GET':
        women_shirts = Women_Shirt.objects.all()
        serializer = WomenShirtSerializer(women_shirts,many=True)
        return Response({'WomenShirts':serializer.data})
    elif request.method == 'POST':
        serializer = WomenShirtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'WomenShirts':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def WomenShirt(request,id):
    try:
        data = Women_Shirt.objects.get(pk=id)
    except Women_Shirt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = WomenShirtSerializer(data)
        return Response({'WomenShirt':serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = WomenShirtSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'WomenShirt':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def WomenJackets(request):
    if request.method == 'GET':
        jackets = Women_Jacket.objects.all()
        serializer = WomenJacketSerializer(jackets,many=True)
        return Response({'WomenJackets': serializer.data})
    elif request.method == 'POST':
        serializer = WomenJacketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'WomenJackets':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def WomenJacket(request,id):
    try:
        data = Women_Jacket.objects.get(pk=id)
    except Women_Jacket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = WomenJacketSerializer(data)
        return Response({'WomenJacket':serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = WomenJacketSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'WomenJacket':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def WomenPants(request):
    if request.method == 'GET':
        womenpants = Women_Pants.objects.all()
        serializer = WomenPantsSerializer(womenpants,many=True)
        return Response({'WomenPants': serializer.data})
    elif request.method == 'POST':
        serializer = WomenPantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'WomenPants':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def WomenPant(request,id):
    try:
        data = Women_Pants.objects.get(pk=id)
    except Women_Pants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = WomenPantsSerializer(data)
        return Response({'WomenPant':serializer.data})
    elif request.method == 'POST':
        serializer = WomenPantsSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'WomenPant':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def WomenJoggers(request):
    if request.method == 'GET':
        joggers = Women_Joggers.objects.all()
        serializer = WomenJoggersSerializer(joggers,many=True)
        return Response({'WomenJoggers': serializer.data})
    elif request.method == 'POST':
        serializer = WomenJoggersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'WomenJoggers':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def WomenJogger(request,id):
    try:
        data = Women_Joggers.objects.get(pk=id)
    except Women_Joggers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = WomenJoggersSerializer(data)
        return Response({'WomenJogger':serializer.data})
    elif request.method == 'POST':
        serializer = WomenJoggersSerializer(data,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'WomenJogger':serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    