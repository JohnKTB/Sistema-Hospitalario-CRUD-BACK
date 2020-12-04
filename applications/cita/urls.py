from django.urls import path

from applications.cita.views import FiltrarCitaxPacienteAPI, FiltrarCitaxFechaAPI

app_name = "cita_app"

urlpatterns = [
    path('api/cita-paciente-filtro/<paciente>', FiltrarCitaxPacienteAPI.as_view(), name='cita_filtro'),
    path('api/filtrar-cita-fecha/<Fecha>', FiltrarCitaxFechaAPI.as_view(), name='filtrar_cita_fecha'),
]
