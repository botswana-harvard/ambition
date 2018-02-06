from ...sites import get_site_id
from ..test.base_test import *

# for django.contrib.sites
SITE_ID = get_site_id('lilongwe')

WSGI_APPLICATION = 'ambition.wsgi.lilongwe.application'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'lilongwe.ambition.clinicedc.org']

TIME_ZONE = 'Africa/Blantyre'
