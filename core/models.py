from django.db import models

class Preinscricao(models.Model):

    OCUPACAO_CHOICES = (
        ('est','Estudante'),
        ('aut','Autônomo'),
        ('mei','MEI (Microempreendedor Individual)'),
        ('mcr', 'Microempresário'),
        ('emg','Empresário de pequeno, médio ou grande porte'),
        ('cl','CLT'),
        ('ou','Outro'),
    )
    GENERO_CHOICES = (
        ('m','Masculino'),
        ('f','Feminino'),
        ('o','Outro'),
    )
    nome = models.CharField(max_length=100, verbose_name='Nome completo')
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    idade = models.IntegerField()
    ocupacao = models.CharField(max_length=3, choices=OCUPACAO_CHOICES)

    class Meta:
        verbose_name = 'Pré-inscrição'
        verbose_name_plural = 'Pré-inscrições'