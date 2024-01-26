from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import TipoComidaViewSet, CategoriaViewSet, MenusViewSet, MostrarMenus, PedirMenuViewSet, MostrarPedidosViewSet, PedirMenuViewSet_2
# ,MostrarCategoriaViewSet, MostrarComidasConCategoriasViewSet

router = DefaultRouter()
router.register(r'tipo_comida', TipoComidaViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'menus', MenusViewSet)
router.register(r'mostrar-pedidos', MostrarPedidosViewSet)
# router.register(r'pedir-menu', PedirMenuViewSet)
# router.register(r'comidaycategorias', MostrarComidasConCategoriasViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/mostar-menu/<int:categoria_id>', MostrarMenus.as_view(), name='mostrar_menus'),
    path('api/pedir-menu', PedirMenuViewSet.as_view(), name='pedir_menus'),
    path('api/pedir-menu-2', PedirMenuViewSet_2.as_view(), name='pedir_menus_2')
    # path('api/mostrarcategorias/<int:tipocomida>', MostrarCategoriaViewSet.as_view(), name='mostarcategorias' ),
    # path('api/mostrarcomidasycategorias/', MostrarComidasConCategoriasViewSet.as_view(), name='mostrarcomidasycategorias' ),
]
