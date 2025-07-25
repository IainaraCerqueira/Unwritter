# Generated by Django 5.2.4 on 2025-07-24 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=150)),
                ('ano_publicacao', models.IntegerField(blank=True, null=True)),
                ('nacionalidade', models.CharField(blank=True, max_length=100)),
                ('sinopse', models.TextField()),
                ('paginas', models.IntegerField()),
                ('tempo_medio_leitura', models.DurationField()),
                ('capa', models.ImageField(blank=True, null=True, upload_to='capas_livros/')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='livros.genero')),
            ],
        ),
    ]
