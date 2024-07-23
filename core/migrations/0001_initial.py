# Generated by Django 4.2.4 on 2024-07-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preinscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp', models.CharField(max_length=20)),
                ('genero', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino'), ('o', 'Outro')], max_length=1)),
                ('idade', models.IntegerField()),
                ('ocupacao', models.CharField(choices=[('est', 'Estudante'), ('aut', 'Autônomo'), ('mei', 'MEI (Microempreendedor Individual)'), ('mcr', 'Microempresário'), ('emg', 'Empresário de pequeno, médio ou grande porte'), ('cl', 'CLT'), ('ou', 'Outro')], max_length=3)),
            ],
            options={
                'verbose_name': 'Pré-inscrição',
                'verbose_name_plural': 'Pré-inscrições',
            },
        ),
    ]
