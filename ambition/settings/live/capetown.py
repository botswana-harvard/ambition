from ...sites import get_site_id
from ..test.base_test import *

# for django.contrib.sites
SITE_ID = get_site_id('capetown')

WSGI_APPLICATION = 'ambition.wsgi.capetown.application'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'capetown.ambition.clinicedc.org']
