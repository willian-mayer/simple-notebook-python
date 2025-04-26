from rest_framework import serializers
from .models import Cuaderno, Hoja, Contenido

class ContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields = '__all__'

class HojaSerializer(serializers.ModelSerializer):
    contenidos = ContenidoSerializer(many=True, read_only=True)

    class Meta:
        model = Hoja
        fields = '__all__'

class CuadernoSerializer(serializers.ModelSerializer):
    hojas = HojaSerializer(many=True, read_only=True)

    class Meta:
        model = Cuaderno
        fields = '__all__'
