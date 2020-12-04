from rest_framework.routers import DefaultRouter

from applications.users.viewsets import userViewset, rolViewset, permisosViewSets

router = DefaultRouter()

router.register(r'user', userViewset, basename='usuario')
router.register(r'rol', rolViewset, basename='rol')
router.register(r'permisos', permisosViewSets, basename='permisos')

urlpatterns = router.urls
