import json
import django
from django.core.wsgi import get_wsgi_application
from django import setup
from django.conf import settings
from django.core.management import call_command
import os

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comida_app.settings')

django.setup()

# call_command('makemigrations', 'comida')
# call_command('migrate')


from comida.models import TipoComida, Categoria, Menus


def limpiar_datos():
    try:
        print('Limpiando datos...')
        TipoComida.objects.all().delete()
        Categoria.objects.all().delete()
        Menus.objects.all().delete()
        print('Datos limpiados ✅')
    except Exception as e:
        print(f"Error al intentar limpiar los datos existentes: {e}")

def insertar_datos_a_la_base(data):
    limpiar_datos()
    try:
        for tipo_almuerzo, sub_categoria in data.items():
            tipo_comida, _ = TipoComida.objects.get_or_create(nombre=tipo_almuerzo)
            for categoria, item_cate in sub_categoria.items():
                categoria, _ = Categoria.objects.get_or_create(tipocomida=tipo_comida, nombre=categoria)
                for item in item_cate:
                    nombre_menu = item.get('producto')
                    precio_menu = item.get('precio')
                    Menus.objects.create(categoria=categoria, nombre=nombre_menu, precio=precio_menu)

        print('Carga de datos exitosa ✅')
    except Exception as e:
        print(f"Error al completar los datos a la base de datos: {e} 🔴")


if __name__ == '__main__':
    with open('data.json') as file:
        data = json.load(file)

    insertar_datos_a_la_base(data)