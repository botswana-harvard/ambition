from .base_test import *

# site is lilongwe
SITE_ID = 30

WSGI_APPLICATION = 'ambition.wsgi.lilongwe-uat.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'lilongwe.uat.ambition.bhp.org.bw']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'uat.conf'),
        },
    },
}

TIME_ZONE = 'Africa/Gaborone'
