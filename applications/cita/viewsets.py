from rest_framework import viewsets, exceptions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from applications.cita.models import cita
from applications.cita.permissions import CitaPermission
from applications.cita.serializers import CitaPagination, citaCreateSerializer, citaDetailSerializer, \
    citaListSerializer


class citaViewSets(viewsets.ModelViewSet):
    serializer_class = citaCreateSerializer
    queryset = cita.objects.all()
    permission_classes = (CitaPermission,)
    pagination_class = CitaPagination

    def permission_denied(self, request, message=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos')

    def list(self, request, *args, **kwargs):
        queryset = cita.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = citaListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = citaListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        citaDetail = get_object_or_404(cita.objects.all(), pk=pk)
        # Deserializamos
        serializer = citaDetailSerializer(citaDetail)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'msj': 'Cita eliminada'
        })
