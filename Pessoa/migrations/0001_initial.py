# Generated by Django 4.0.5 on 2022-06-22 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField()),
                ('telefone', models.CharField(max_length=11)),
                ('cep', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=50)),
            ],
        ),
    ]
