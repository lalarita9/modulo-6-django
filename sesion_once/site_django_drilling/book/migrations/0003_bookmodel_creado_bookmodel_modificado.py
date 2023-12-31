# Generated by Django 4.2.2 on 2023-06-26 02:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_bookmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
