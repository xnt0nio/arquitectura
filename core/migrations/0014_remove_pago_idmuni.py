# Generated by Django 4.2.7 on 2023-11-26 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_rename_id_bono_idbono_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='idMuni',
        ),
    ]