import os

from Hospital.settings.base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'mysql_cymysql',
        'NAME': 'dbhospital',
        'USER': 'root',
        'PASSWORD': 'samanthafox',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]