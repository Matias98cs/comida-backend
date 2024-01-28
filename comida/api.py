from .models import TipoComida, Categoria, Menus, Pedido
from rest_framework import viewsets, permissions, status
from .serializers import ComidaSerializer, CategoriaSerializer, MenusSerializer, PedirMenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


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
        pedidos = Pedido.objects.all().order_by('-hora_pedido') [:3] #obtiene 3 registros
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

