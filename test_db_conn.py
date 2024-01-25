import django
from django.core.wsgi import get_wsgi_application
from django import setup
from django.conf import settings
from django.core.management import call_command
import os

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comida_app.settings')

django.setup()

call_command('makemigrations', 'comida')
call_command('migrate')


from comida.models import TipoComida

try:
    # Intentar realizar una consulta simple
    resultados = TipoComida.objects.first()
    print("Conexión a la base de datos exitosa. 🟢")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e} 🔴")
