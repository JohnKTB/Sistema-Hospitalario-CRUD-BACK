from django.contrib.auth.models import Permission
from rest_framework import viewsets, exceptions
from rest_framework.response import Response

from applications.users.models import User, Rol
from applications.users.permissions import UserPermission
from applications.users.serializers import userListaSerializer, RolSerializer, createUserSerializer, permisosSerializer


class rolViewset(viewsets.ModelViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = RolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'msj': 'Ok'
        })


class userViewset(viewsets.ModelViewSet):
    serializer_class = createUserSerializer
    queryset = User.objects.all()
    permission_classes = (UserPermission,)

    def permission_denied(self, request, message=None):

        if request.authenticators and not request.successful_authenticator:
            raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail='No tiene permisos')

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = userListaSerializer(queryset, many=True)
        # serializer.data --> los datos que se han serializado
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = createUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create(
            username=serializer.validated_data['username'],
            is_staff=False,
            is_superuser=False,
            email=serializer.validated_data['email'],
        )
        id = serializer.data['user_permissions']
        for elemento in id:
            usuario = User.objects.get(username=serializer.validated_data['username'])
            usuario.user_permissions.add(elemento)
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response({
            'msj': 'Usuario Agregado!'
        })


class permisosViewSets(viewsets.ModelViewSet):
    serializer_class = permisosSerializer
    queryset = Permission.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Permission.objects.exclude(id__lte=20)
        serializer = permisosSerializer(queryset, many=True)
        return Response(serializer.data)
