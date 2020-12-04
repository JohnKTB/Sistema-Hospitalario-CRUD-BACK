from rest_framework.routers import DefaultRouter

from applications.doctor.viewsets import DoctorViewSet

router = DefaultRouter()

router.register(r'doctor', DoctorViewSet, basename='doctor')

urlpatterns = router.urls
