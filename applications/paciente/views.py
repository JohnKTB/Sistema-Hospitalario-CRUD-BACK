from rest_framework.generics import ListAPIView

from applications.paciente.models import paciente
from applications.paciente.serializers import PacienteSerializer


class FiltrarPacienteAPI(ListAPIView):
    serializer_class = PacienteSerializer
    queryset = paciente.objects.all().order_by('id')
 
    def get_queryset(self):
        letras = self.kwargs['nombre']
        return paciente.objects.filter(full_name__icontains=letras)[:10]
