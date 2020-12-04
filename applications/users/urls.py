from django.urls import path

from applications.users.views import listaPermisosApiView

app_name = "user_app"

urlpatterns = [
    path('api/list-permisos/', listaPermisosApiView.as_view(), name='list_permisos'),
]
