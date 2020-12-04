from django.urls import path

from applications.doctor.views import especialidadesListAPIView, FiltrarDoctorAPI, DoctorDetalAPI, \
    DoctorxEspecialidadAPI

app_name = "doctor_app"

urlpatterns = [
    path('api/especialidades/', especialidadesListAPIView.as_view(), name='especialidades'),
    path('api/doctor-filtro/<nombre>', FiltrarDoctorAPI.as_view(), name='doctor_filtro'),
    path('api/doctor-por-especialidad/<especialidad>', DoctorxEspecialidadAPI.as_view(), name='doctor_por_especialidad'),
    path('api/doctor-detail/<pk>', DoctorDetalAPI.as_view(), name='doctor_detail'),
]
