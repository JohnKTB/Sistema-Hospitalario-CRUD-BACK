from django.db import models
from model_utils.models import TimeStampedModel


class persona(TimeStampedModel):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    full_name = models.CharField('nombre y apellido', max_length=120, blank=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=150, blank=True, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.apellido} - {self.full_name} - {self.telefono} - {self.email}'


class paciente(persona):
    edad = models.PositiveIntegerField()
    direccion = models.CharField(max_length=200)
    dni = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'paciente'

    def __str__(self):
        return super().__str__() + ' - ' + str(self.edad)
