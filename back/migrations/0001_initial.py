# Generated by Django 4.0.5 on 2022-06-16 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
