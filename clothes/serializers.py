from rest_framework import serializers
from clothes.models import Men_Shirt,Men_Jacket,Men_Pants,Men_Joggers,Glasses,Earring,Necklace,Women_Shirt,Women_Jacket,Women_Pants,Women_Joggers
class MenShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Men_Shirt 
        fields = '__all__'

class MenJacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Men_Jacket
        fields = '__all__'

class MenPantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Men_Pants
        fields = '__all__'

class MenJoggersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Men_Joggers
        fields = '__all__'

class GlassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glasses
        fields = '__all__'

class EarringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earring
        fields = '__all__'

class NecklaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Necklace
        fields = '__all__'

class WomenShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women_Shirt
        fields = '__all__'
    
class  WomenJacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women_Jacket
        fields = '__all__'

class WomenPantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women_Pants
        fields = '__all__'

class WomenJoggersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women_Joggers
        fields = '__all__'

