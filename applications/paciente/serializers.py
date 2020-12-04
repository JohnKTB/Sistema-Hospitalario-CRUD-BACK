from rest_framework import serializers, pagination

from applications.paciente.models import paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = paciente
        fields = (
            'id',
            'full_name',
            'telefono',
            'email',
            'edad',
            'direccion',
            'dni'
        )

    def validate_edad(self, value):
        if value < 0:
            raise serializers.ValidationError('Coloque una edad valida!')


class PacienteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = paciente
        fields = (
            'id',
            'nombre',
            'apellido',
            'telefono',
            'email',
            'edad',
            'direccion',
            'dni'
        )


class PacientePagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100
