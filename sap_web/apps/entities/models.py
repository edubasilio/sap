from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nome')


    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
    
    def __str__(self):
        return f'{self.name}'
