from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Cuaderno, Hoja, Contenido
from .serializers import CuadernoSerializer, HojaSerializer, ContenidoSerializer

class CuadernoViewSet(viewsets.ModelViewSet):
    queryset = Cuaderno.objects.all()
    serializer_class = CuadernoSerializer

class HojaViewSet(viewsets.ModelViewSet):
    queryset = Hoja.objects.all()
    serializer_class = HojaSerializer

class ContenidoViewSet(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer
