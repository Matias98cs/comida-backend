from rest_framework import serializers
from django.utils import timezone
from .models import TipoComida, Categoria, Pedido, Menus


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ComidaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(many=True, read_only=True)
    class Meta:
        model = TipoComida
        fields = "__all__"

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = "__all__"

class PedirMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['hora_pedido'] = timezone.localtime(instance.hora_pedido).strftime('%Y-%m-%d %H:%M:%S')
        return representation