from rest_framework import serializers, pagination

from applications.doctor.models import doctor, especialidad


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = especialidad
        fields = (
            'id',
            'descripcion'
        )


class DoctorSerializer(serializers.ModelSerializer):
    especialidad = EspecialidadSerializer()

    class Meta:
        model = doctor
        fields = (
            'id',
            'nombre',
            'apellido',
            'full_name',
            'telefono',
            'email',
            'especialidad',
        )


class DoctorxEspecialidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = doctor
        fields = (
            'id',
            'full_name'
        )


class DoctorUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = doctor
        fields = (
            'id',
            'nombre',
            'apellido',
            'full_name',
            'telefono',
            'email',
            'especialidad',
        )


class DoctorPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100
