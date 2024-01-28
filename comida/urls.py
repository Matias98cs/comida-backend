from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import TipoComidaViewSet, MostrarMenus, PedirMenuViewSet_2

router = DefaultRouter()
router.register(r'tipo_de_comida', TipoComidaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/mostar-menu/', MostrarMenus.as_view(), name='mostrar_menus'),
    path('api/pedir-menu', PedirMenuViewSet_2.as_view(), name='pedir_menus')
]
