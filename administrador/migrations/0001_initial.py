# Generated by Django 4.0.5 on 2022-06-28 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]