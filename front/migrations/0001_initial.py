# Generated by Django 4.0.5 on 2022-06-16 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreImagen', models.CharField(max_length=250)),
                ('marca', models.CharField(max_length=100)),
                ('nombreProducto', models.CharField(max_length=100)),
                ('precio', models.IntegerField(max_length=100)),
            ],
        ),
    ]
