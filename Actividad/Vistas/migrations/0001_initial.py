# Generated by Django 3.2.6 on 2021-09-10 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('nacimineto', models.DateField()),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actulizacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]