from rest_framework import serializers
from .models import *
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['mens_shirts','mens_jackets','mens_pants','mens_joggers',
                  'glasses','earrings','necklaces','women_shirts','women_jackets',
                  'women_pants','women_joggers']