from django.shortcuts import get_object_or_404
from rest_framework import viewsets, exceptions
from rest_framework.response import Response

from applications.paciente.models import paciente
from applications.paciente.permissions import PacientePermission
from applications.paciente.serializers import PacienteSerializer, PacientePagination, PacienteDetailSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = paciente.objects.all()
    permission_classes = (PacientePermission,)
    pagination_class = PacientePagination

    def permission_denied(self, request, message=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos')

    def list(self, request, *args, **kwargs):
        queryset = paciente.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PacienteSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PacienteSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        pacien = get_object_or_404(paciente.objects.all(), pk=pk)
        # Deserializamos
        serializer = PacienteDetailSerializer(pacien)
        return Response(serializer.data)

    def perform_update(self, serializer):
        nombre = self.request.data['nombre']
        apellido = self.request.data['apellido']
        serializer.save(
            full_name=nombre + ' ' + apellido
        )

    def perform_create(self, serializer):
        nombre = self.request.data['nombre']
        apellido = self.request.data['apellido']
        serializer.save(
            full_name=nombre + ' ' + apellido
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'msj': 'Paciente eliminado'
        })
