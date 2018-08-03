from .base_test import *

# site is mbarara
SITE_ID = 70

WSGI_APPLICATION = 'ambition.wsgi.mbarara-uat.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'mbarara.uat.ambition.bhp.org.bw']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'uat.conf'),
        },
    },
}

TIME_ZONE = 'Africa/Mbarara'
