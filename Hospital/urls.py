
from django.contrib import admin
from django.urls import path, re_path, include
# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# JWT
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from applications.users.views import MyTokenObtainPairView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ends here

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.doctor.routers')),
    re_path('', include('applications.doctor.urls')),
    re_path('', include('applications.users.routers')),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.paciente.urls')),
    re_path('', include('applications.paciente.routers')),
    re_path('', include('applications.cita.urls')),
    re_path('', include('applications.cita.routers')),

    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  # <-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  # <-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  # <-- Here

    # JWT
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
