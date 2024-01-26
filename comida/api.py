from .models import TipoComida, Categoria, Menus, Pedido
from rest_framework import viewsets, permissions, status
from .serializers import ComidaSerializer, CategoriaSerializer, MenusSerializer, PedirMenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError


class TipoComidaViewSet(viewsets.ModelViewSet):
    queryset = TipoComida.objects.all()
    serializer_class = ComidaSerializer

class MostrarMenus(APIView):
    def get(self, request, *args, **kwargs):
        tipo_comida =  request.query_params.get('tipo_comida', None)
        categoria = request.query_params.get('categoria', None)        
        try:    
            menus = Menus.objects.filter(categoria__tipocomida__nombre=tipo_comida, categoria__nombre=categoria)
            if not menus.exists():
                return Response({"msj": "No se encontraron menus para esos datos"}, status=status.HTTP_404_NOT_FOUND)
            serializer = MenusSerializer(menus, many=True).data
            return Response({"msj": "Mostrando menus", "data": serializer}, status=status.HTTP_200_OK)
        except Menus.DoesNotExist:
            return Response({"msj": "Hubo un error al obtener los menus"}, status=status.HTTP_404_NOT_FOUND)
        
class PedirMenuViewSet_2(APIView):
    def get(self, request):
        pedidos = Pedido.objects.all().order_by('-hora_pedido') #[:3] obtiene 3 registros
        serializer = PedirMenuSerializer(pedidos, many=True).data
        return Response({"msj": "Pedidos", "data": serializer}, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        pedido = request.data
        pedido_id = pedido.get('menu_id')
        if not pedido_id:
            return Response({"msj": "Debe mandar el id del menu para pedir"})
    
        try:
            menu = Menus.objects.get(id=pedido_id)
            menu_serialize = MenusSerializer(menu).data
            crear_pedido = Pedido.objects.create(nombre=menu_serialize['nombre'], precio=menu_serialize['precio'])
            pedido_serealizer = PedirMenuSerializer(crear_pedido).data
            return Response({"msj": "Producto pedido con exito", "data": pedido_serealizer}, status=status.HTTP_201_CREATED)
        except Menus.DoesNotExist:
            return Response({"msj": "Hubo un error al pedir su producto"}, status=status.HTTP_400_BAD_REQUEST)

# class CategoriaViewSet(viewsets.ModelViewSet):
#     queryset = Categoria.objects.all()
#     serializer_class = CategoriaSerializer

# class MenusViewSet(viewsets.ModelViewSet):
#     queryset = Menus.objects.all()
#     serializer_class = MenusSerializer



# class PedirMenuViewSet(APIView):
#     def post(self, request, *args, **kwargs):
#         pedido_cliente = request.data
#         if not all(value != '' for value in pedido_cliente.values()):
#             print('Debe completar todos los campos')
#             return Response({"msj": "Debe ingresar todos los campos", "estado":status.HTTP_400_BAD_REQUEST})
        
#         crear_pedido = Pedido.objects.create(nombre=pedido_cliente['nombre'], precio=pedido_cliente['precio'])
#         pedido_serializer = PedirMenuSerializer(crear_pedido).data
#         return Response({"msj": "Menu pedido", "data": pedido_serializer})
    
# class MostrarPedidosViewSet(viewsets.ModelViewSet):
#     queryset = Pedido.objects.all().order_by('-hora_pedido') #[:3] obtiene 3 registros
#     serializer_class = PedirMenuSerializer


        
# class MostrarCategoriaViewSet(APIView):
#     def get(self, request, tipocomida, format=None):
#         print(f"El parametro es {tipocomida}")
#         categorias = Categoria.objects.filter(tipocomida=tipocomida)
#         serializer = CategoriaSerializer(categorias, many=True)

#         return Response({"msj": f"Comidas para {tipocomida}", "data": serializer.data, "status": status.HTTP_200_OK})

# class MostrarComidasConCategoriasViewSet(viewsets.ModelViewSet):
#     tipocomida = TipoComida.objects.all()
#     serializer = ComidaSerializer(instance=tipocomida, many=True)
    # serializer.data
     
# class MostrarComidasConCategoriasViewSet(APIView):
#     def get(self, request, format=None):
#         print('Mostrar comidas con sus categorias')
#         tipos_comidas = TipoComida.objects.prefetch_related('categoria')
#         serializer = ComidaSerializer(tipos_comidas, many=True).data
#         return Response({"msj": "Todas las comidas y sus categorías", "data": serializer})
    # def get(self, request, format=None):
    #     print(f"Mostrando todas las comidas y categorias")
    #     tipos_comida = TipoComida.objects.all()
    #     data = {}

    #     for tipo_comida in tipos_comida:
    #         categorias = tipo_comida.categoria_set.all()
    #         serializer = CategoriaSerializer(categorias, many=True)
    #         data[tipo_comida.nombre] = serializer.data

    #     return Response({"msj": "Todas las comidas y sus categorias", "data": data})

