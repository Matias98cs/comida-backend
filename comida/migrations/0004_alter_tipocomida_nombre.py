# Generated by Django 5.0.1 on 2024-01-24 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comida', '0003_alter_tipocomida_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipocomida',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
