from .base import *

DEBUG = False

ETC_DIR = os.path.join('/etc', APP_NAME)

SECRET_KEY = '2^p0phb&x&ntbsduf6afw(@efi(+!&hm_lrjr-+$5v(t0_f+6t'
SITE_ID = '10'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'ambition-test.bhp.org.bw']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(ETC_DIR, 'mysql.conf'),
        },
    },
}

STATIC_ROOT = os.path.join(str(Path(BASE_DIR).parent), 'static')
KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')
