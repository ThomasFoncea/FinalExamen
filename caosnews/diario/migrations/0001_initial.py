# Generated by Django 4.1.2 on 2023-07-14 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCategoria',
            fields=[
                ('idCategoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='noticias',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='codigo')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('fecha', models.CharField(max_length=10, null=True, verbose_name='fecha')),
                ('titulo', models.CharField(max_length=50, verbose_name='titulo')),
                ('cuerpo', models.CharField(max_length=600, verbose_name='Cuerpo')),
                ('Img', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='img')),
                ('idCategoria', models.ForeignKey(db_column='idCategoria', on_delete=django.db.models.deletion.CASCADE, to='diario.areacategoria', verbose_name='idCategoria')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
