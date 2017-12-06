from .base import *

DEBUG = False

ETC_DIR = os.path.join('/etc', APP_NAME)

# move to a file in /etc  !!!!!!!!!!!!!!!!!!!!!!
SECRET_KEY = '2^p0phb&x&ntbsduf6afw(@efi(+!&hm_lrjr-+$5v(t0_f+6t'

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
AUTO_CREATE_KEYS = False

EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USB_VOLUME = None
