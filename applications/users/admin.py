from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from applications.users.models import User, Rol

admin.site.register(Rol)
admin.site.register(User)
admin.site.register(Permission)
admin.site.register(ContentType)
