from django.db import models

class Consulta(models.Model):
    STATUS_CHOICES = (
        ('A', 'Agendada'),
        ('C', 'Cancelada'),
    )

    medico = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
