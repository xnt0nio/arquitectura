# Generated by Django 4.2.7 on 2023-11-26 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_contactform_tipoproducto_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bono',
            old_name='Id',
            new_name='Idbono',
        ),
        migrations.RenameField(
            model_name='postulacion_taller',
            old_name='Id',
            new_name='Idpostulacion',
        ),
        migrations.RenameField(
            model_name='sala',
            old_name='Id',
            new_name='Idsala',
        ),
        migrations.RenameField(
            model_name='talleres',
            old_name='Id',
            new_name='Idtalleres',
        ),
    ]