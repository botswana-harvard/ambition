from ..live.base_live import *

# site is gaborone
SITE_ID = 10

WSGI_APPLICATION = 'ambition.wsgi.l2.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'l2.ambition.bhp.org.bw']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'live_2.conf'),
        },
    },
}
