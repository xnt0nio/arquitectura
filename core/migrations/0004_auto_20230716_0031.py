# Generated by Django 3.1.2 on 2023-07-16 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230714_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='asunto',
            field=models.CharField(max_length=100),
        ),
    ]
