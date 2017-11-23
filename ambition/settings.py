import os
import sys

from django.core.management.color import color_style

from .logging import LOGGING

style = color_style()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = 'ambition'

logging_handler = LOGGING.get('handlers').get('file').get('filename')
sys.stdout.write(style.SUCCESS(f'Logging to {logging_handler}\n'))


DEBUG = True

ETC_DIR = os.path.join(BASE_DIR, 'etc')

SECRET_KEY = '2^p0phb&x&ntbsduf6afw(@efi(+!&hm_lrjr-+$5v(t0_f+6t'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'django_js_reverse',
    'django_extensions',
    'crispy_forms',
    'tz_detect',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'edc_model_admin.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_facility.apps.AppConfig',
    'edc_form_validators.apps.AppConfig',
    'edc_fieldsets.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_lab_dashboard.apps.AppConfig',
    'edc_sync.apps.AppConfig',
    'edc_sync_files.apps.AppConfig',
    'edc_pharmacy.apps.AppConfig',
    'edc_pharmacy_dashboard.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'ambition_dashboard.apps.AppConfig',
    'ambition_labs.apps.AppConfig',
    'ambition_metadata_rules.apps.AppConfig',
    'ambition_rando.apps.AppConfig',
    'ambition_reference.apps.AppConfig',
    'ambition_subject.apps.AppConfig',
    'ambition_validators.apps.AppConfig',
    'ambition_visit_schedule.apps.AppConfig',
    'ambition.apps.EdcAppointmentAppConfig',
    'ambition.apps.EdcBaseAppConfig',
    'ambition.apps.EdcDeviceAppConfig',
    'ambition.apps.EdcIdentifierAppConfig',
    'ambition.apps.EdcLabAppConfig',
    'ambition.apps.EdcLabelAppConfig',
    'ambition.apps.EdcMetadataAppConfig',
    'ambition.apps.EdcProtocolAppConfig',
    'ambition.apps.EdcVisitTrackingAppConfig',
    'ambition.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ambition.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ambition.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(ETC_DIR, 'mysql.conf'),
        },
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('af', 'Afrikaans'),
    ('ny', 'Chichewa'),
    ('en', 'English'),
    ('xh', 'isiXhosa'),
    ('lg', 'Luganda'),
    ('rny', 'Runyankore'),
    ('tn', 'Setswana'),
    ('sn', 'Shona'))

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%d/%m/%Y %H:%M:%S',     # '25/10/2006 14:30:59'
    '%d/%m/%Y %H:%M:%S.%f',  # '25/10/2006 14:30:59.000200'
    '%d/%m/%Y %H:%M',        # '25/10/2006 14:30'
    '%d/%m/%Y',              # '25/10/2006'
]
DATE_INPUT_FORMATS = ['%Y-%m-%d', '%d/%m/%Y']

DATETIME_FORMAT = 'j N Y P'
DATE_FORMAT = 'j N Y'
SHORT_DATETIME_FORMAT = 'd/m/Y P'
SHORT_DATE_FORMAT = 'd/m/Y'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'ambition', 'static')
GIT_DIR = BASE_DIR
KEY_PATH = os.path.join(BASE_DIR, 'crypto_fields')

EDC_LAB_REQUISITION_MODEL = 'ambition_subject.subjectrequisition'
LABEL_PRINTER = 'test_label_printer_ambition'
# EDC_PHARMA_PRESCRIPTION_MODEL = 'edc_pharmacy.prescription'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MAIN_NAVBAR_NAME = APP_NAME

EDC_SYNC_SERVER_IP = None
EDC_SYNC_FILES_REMOTE_HOST = None
EDC_SYNC_FILES_USER = None
EDC_SYNC_FILES_USB_VOLUME = None

DEFAULT_APPOINTMENT_MODEL = 'edc_appointment.appointment'
HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')
COUNTRY = 'botswana'

if 'test' in sys.argv:

    class DisableMigrations:

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher', )
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
