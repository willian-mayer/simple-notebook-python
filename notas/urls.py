from django.urls import include, path
from rest_framework import routers
from .views import CuadernoViewSet, HojaViewSet, ContenidoViewSet

router = routers.DefaultRouter()
router.register(r'cuadernos', CuadernoViewSet)
router.register(r'hojas', HojaViewSet)
router.register(r'contenidos', ContenidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
