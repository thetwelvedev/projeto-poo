# Generated by Django 5.1.6 on 2025-03-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50, unique=True)),
                ('senha', models.CharField(max_length=50)),
                ('primeiro_nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('numero_cartao', models.CharField(max_length=19)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('endereco', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
    ]
