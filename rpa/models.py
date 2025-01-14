from django.db import models
from django.contrib import admin

# Modelo da tabela Aprovacao
class Aprovacao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
    ]

    cpf = models.CharField(max_length=11, verbose_name='CPF')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pendente',
        verbose_name='Status'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Aprovação'
        verbose_name_plural = 'Aprovações'

    def __str__(self):
        return f"{self.cpf} - {self.status}"