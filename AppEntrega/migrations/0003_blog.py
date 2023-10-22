# Generated by Django 4.2.5 on 2023-10-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega', '0002_alter_profesor_apellido_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=15)),
                ('subTitulo', models.CharField(max_length=30)),
                ('cuerpo', models.CharField(max_length=300)),
                ('autor', models.CharField(max_length=20)),
                ('fecha', models.DateTimeField()),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]