from datetime import date, datetime
from django.db import models
from model_utils.models import TimeStampedModel

from applications.doctor.models import doctor
from applications.paciente.models import paciente


class cita(TimeStampedModel):
    fecha_atencion = models.DateTimeField()
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE, null=True)
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'cita'
        verbose_name_plural = 'citas'
        db_table = 'cita'

    def __str__(self):
        return f'{self.doctor} - {self.paciente} - {self.fecha_atencion}'
