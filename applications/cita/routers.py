from rest_framework.routers import DefaultRouter

from applications.cita.viewsets import citaViewSets

router = DefaultRouter()

router.register(r'cita', citaViewSets, basename='cita')

urlpatterns = router.urls
