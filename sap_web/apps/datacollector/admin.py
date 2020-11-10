from django.contrib import admin

from .models import MedicalExam, ClinicalMonitoring


admin.site.register(MedicalExam)
admin.site.register(ClinicalMonitoring)
