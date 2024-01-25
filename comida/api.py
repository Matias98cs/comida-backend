from .models import TipoComida, Categoria, Menus, Pedido
from rest_framework import viewsets, permissions, status
from .serializers import ComidaSerializer, CategoriaSerializer, MenusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError


class TipoComidaViewSet(viewsets.ModelViewSet):
    queryset = TipoComida.objects.all()
    serializer_class = ComidaSerializer
    # permission_classes = [permissions.AllowAny]

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MenusViewSet(viewsets.ModelViewSet):
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer

class MostrarMenus(APIView):
    def get(self, request, categoria_id=None, **kwargs):
        if categoria_id is None:
            return Response({"msj": "Por favor, proporciona una categoría válida en la URL."}, status=status.HTTP_400_BAD_REQUEST)

        print(categoria_id)
        menu = Menus.objects.filter(categoria_id=categoria_id)
        serializer = MenusSerializer(menu, many=True).data
        return Response({"msj": "Probando la ruta para mostrar los menus", "data": serializer})



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

