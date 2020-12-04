from rest_framework import permissions


class CitaPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('cita.view_cita')
        elif request.method == 'PUT':
            return request.user.has_perm('cita.change_cita')
        elif request.method == 'POST':
            return request.user.has_perm('cita.add_cita')
        elif request.method == 'DELETE':
            return request.user.has_perm('cita.delete_cita')
        return False
