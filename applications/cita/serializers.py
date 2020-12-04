
from rest_framework import serializers, pagination

from applications.cita.models import cita
from applications.doctor.models import doctor
from applications.paciente.models import paciente


class pacienteNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = paciente
        fields = (
            'id',
            'full_name'
        )


class doctorNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = (
            'id',
            'full_name'
        )


class citaListSerializer(serializers.ModelSerializer):
    doctor = doctorNombreSerializer()
    paciente = pacienteNombreSerializer()
    fecha_atencion = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = cita
        fields = (
            'id',
            'fecha_atencion',
            'doctor',
            'paciente'
        )


class citaDetailSerializer(serializers.ModelSerializer):
    doctor = doctorNombreSerializer()
    paciente = pacienteNombreSerializer()
    fecha_atencion = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")

    class Meta:
        model = cita
        fields = (
            'id',
            'fecha_atencion',
            'doctor',
            'paciente'
        )


class citaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = cita
        fields = '__all__'


class CitaPagination(pagination.PageNumberPagination):
    page_size = 10
