from django.db import models

from entities.models import Patient


MEDICAL_EXAM_CHOICES = [
    ('0', 'Emoglobina'),
    ('1', 'Leucocitos'),
    ('2', 'Plaquetas'),
]

BODY_WEGHT_CHOICES = [
    ('0', 'Manutenção do Peso'),
    ('1', 'Perda de Peso'),
    ('2', 'Ganho de Peso'),
]

class MedicalExam(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    exam = models.CharField(max_length=2, choices=MEDICAL_EXAM_CHOICES, verbose_name='Exame')
    result = models.FloatField(verbose_name='Resultado')    

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'
    
    def __str__(self):
        return f'{self.exam}'


class ClinicalMonitoring(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    visual_change = models.BooleanField(verbose_name='Alterações Visuais')
    body_weight = models.CharField(max_length=1, choices=BODY_WEGHT_CHOICES, verbose_name='Peso Corporal')

    class Meta:
        verbose_name = 'Acompanhamento Clínico'
        verbose_name_plural = 'Acompanhamentos Clínicos'
    
    def __str__(self):
        return f'{self.patient}'