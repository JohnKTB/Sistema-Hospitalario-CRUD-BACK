from rest_framework import permissions


class PacientePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('paciente.view_paciente')
        elif request.method == 'PUT':
            return request.user.has_perm('paciente.change_paciente')
        elif request.method == 'POST':
            return request.user.has_perm('paciente.add_paciente')
        elif request.method == 'DELETE':
            return request.user.has_perm('paciente.delete_paciente')
        return False
