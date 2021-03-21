# Generated by Django 3.1.7 on 2021-03-20 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme', models.CharField(max_length=50)),
                ('finalizado', models.BooleanField(verbose_name='Finalizado')),
                ('resenha', models.CharField(max_length=255)),
                ('sinopse', models.CharField(max_length=255)),
            ],
        ),
    ]
