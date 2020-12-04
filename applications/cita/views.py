from rest_framework.generics import ListAPIView

from applications.cita.models import cita
from applications.cita.serializers import citaListSerializer


class FiltrarCitaxPacienteAPI(ListAPIView):
    serializer_class = citaListSerializer

    def get_queryset(self):
        letras = self.kwargs['paciente']
        return cita.objects.filter(paciente__full_name__icontains=letras)[:10]


class FiltrarCitaxFechaAPI(ListAPIView):
    serializer_class = citaListSerializer

    def get_queryset(self):
        fecha = self.kwargs['Fecha']
        return cita.objects.filter(fecha_atencion__icontains=fecha)[:10]
