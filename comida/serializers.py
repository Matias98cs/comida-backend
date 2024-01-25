from rest_framework import serializers
from .models import TipoComida, Categoria, Pedido, Menus


class ComidaSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField(many=True)
    class Meta:
        model = TipoComida
        fields = "__all__"

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = "__all__"