from rest_framework.generics import ListAPIView, RetrieveAPIView

from applications.doctor.models import especialidad, doctor
from applications.doctor.serializers import EspecialidadSerializer, DoctorSerializer, DoctorxEspecialidadSerializer


class especialidadesListAPIView(ListAPIView):
    serializer_class = EspecialidadSerializer
    queryset = especialidad.objects.all().order_by('id')


class FiltrarDoctorAPI(ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        letras = self.kwargs['nombre']
        return doctor.objects.filter(full_name__icontains=letras)[:10]


class DoctorDetalAPI(RetrieveAPIView):
    serializer_class = DoctorSerializer
    queryset = doctor.objects.all()


class DoctorxEspecialidadAPI(ListAPIView):
    serializer_class = DoctorxEspecialidadSerializer

    def get_queryset(self):
        Espec = self.kwargs['especialidad']
        return doctor.objects.filter(especialidad__descripcion__icontains=Espec)
