from .base_test import *

# site is harare
SITE_ID = 20

WSGI_APPLICATION = 'ambition.wsgi.harare-uat.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'harare.uat.ambition.bhp.org.bw']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'uat.conf'),
        },
    },
}

TIME_ZONE = 'Africa/harare'
