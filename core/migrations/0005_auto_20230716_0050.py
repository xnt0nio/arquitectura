# Generated by Django 3.1.2 on 2023-07-16 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230716_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='agregados',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_agregados',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
