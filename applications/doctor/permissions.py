from rest_framework import permissions


class DoctorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('doctor.view_doctor')
        elif request.method == 'PUT':
            return request.user.has_perm('doctor.change_doctor')
        elif request.method == 'POST':
            return request.user.has_perm('doctor.add_doctor')
        elif request.method == 'DELETE':
            return request.user.has_perm('doctor.delete_doctor')
        return False
