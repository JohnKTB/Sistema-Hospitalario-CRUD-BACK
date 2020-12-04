from django.db import models
from model_utils.models import TimeStampedModel

from applications.paciente.models import persona


class especialidad(TimeStampedModel):
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'especialidad'
        verbose_name_plural = 'especialidades'
        db_table = 'especialidad'

    def __str__(self):
        return f'{self.id} - {self.descripcion}'


class doctor(persona):
    especialidad = models.ForeignKey(especialidad, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctores'
        db_table = 'doctor'

    def __str__(self):
        return super().__str__() + ' - ' + str(self.especialidad)
