# Generated by Django 5.0.6 on 2024-08-12 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_capital_historialcapital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capital',
            name='monto_inicial',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
