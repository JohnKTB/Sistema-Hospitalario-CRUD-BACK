from django.urls import path

from applications.paciente.views import FiltrarPacienteAPI

app_name = "paciente_app"

urlpatterns = [
    path('api/filtrar-paciente/<nombre>', FiltrarPacienteAPI.as_view(), name='filtrar_paciente'),

]
