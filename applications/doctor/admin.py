from django.contrib import admin

from applications.doctor.models import especialidad, doctor

admin.site.register(especialidad)
admin.site.register(doctor)
