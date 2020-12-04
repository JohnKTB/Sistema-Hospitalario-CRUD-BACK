
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from applications.users.serializers import MyTokenObtainPairSerializer, permisosSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class listaPermisosApiView(ListAPIView):
    serializer_class = permisosSerializer
