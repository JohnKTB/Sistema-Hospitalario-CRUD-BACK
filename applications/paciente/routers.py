from rest_framework.routers import DefaultRouter

from applications.paciente.viewsets import PacienteViewSet

router = DefaultRouter()

router.register(r'paciente', PacienteViewSet, basename='paciente')

urlpatterns = router.urls
