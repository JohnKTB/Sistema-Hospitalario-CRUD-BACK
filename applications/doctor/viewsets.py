from rest_framework import viewsets, exceptions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from applications.doctor.models import doctor
from applications.doctor.permissions import DoctorPermission
from applications.doctor.serializers import DoctorSerializer, DoctorPagination, \
    DoctorUpdateSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorUpdateSerializer
    pagination_class = DoctorPagination
    permission_classes = (DoctorPermission, )

    def permission_denied(self, request, message=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos')

    def get_queryset(self):
        return doctor.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = doctor.objects.all().order_by('id')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = DoctorSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = DoctorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        citaDetail = get_object_or_404(doctor.objects.all(), pk=pk)
        # Deserializamos
        serializer = DoctorSerializer(citaDetail)
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
            'msj': 'Doctor eliminado'
        })

