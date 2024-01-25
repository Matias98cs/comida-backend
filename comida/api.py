from .models import TipoComida, Categoria, Menus, Pedido
from rest_framework import viewsets, permissions, status
from .serializers import ComidaSerializer, CategoriaSerializer, MenusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


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

class MostrarCategoriaViewSet(APIView):
    def get(self, request, tipocomida, format=None):
        print(f"El parametro es {tipocomida}")
        categorias = Categoria.objects.filter(tipocomida=tipocomida)
        serializer = CategoriaSerializer(categorias, many=True)

        return Response({"msj": f"Comidas para {tipocomida}", "data": serializer.data, "status": status.HTTP_200_OK})

# class MostrarComidasConCategoriasViewSet(viewsets.ModelViewSet):
#     queryset = TipoComida.objects.all()
#     serializer_class = ComidaSerializer

#     def list(self, request, *args, **kwargs):
#         tipos_comida = self.get_queryset()
#         serializer = self.get_serializer(tipos_comida, many=True)
#         data = serializer.data
#         for tipo_comida, serialized_data in zip(tipos_comida, data):
#             categorias = tipo_comida.categoria_set.all()
#             categorias_data = CategoriaSerializer(categorias, many=True).data
#             serialized_data['categorias'] = categorias_data
#         return Response({"mensaje": "Comidas con sus categorías", "data": data})
class MostrarComidasConCategoriasViewSet(APIView):
    def get(self, request, format=None):
        tipos_comidas = TipoComida.objects.prefetch_related('categoria')
        serializer = ComidaSerializer(tipos_comidas, many=True).data
        return Response({"msj": "Todas las comidas y sus categorías", "data": serializer})
    # def get(self, request, format=None):
    #     print(f"Mostrando todas las comidas y categorias")
    #     tipos_comida = TipoComida.objects.all()
    #     data = {}

    #     for tipo_comida in tipos_comida:
    #         categorias = tipo_comida.categoria_set.all()
    #         serializer = CategoriaSerializer(categorias, many=True)
    #         data[tipo_comida.nombre] = serializer.data

    #     return Response({"msj": "Todas las comidas y sus categorias", "data": data})

