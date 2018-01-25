from ...sites import get_site_id
from .base_test import *

# for django.contrib.sites
SITE_ID = get_site_id('lilongwe')

WSGI_APPLICATION = 'ambition.wsgi.lilongwe.application'
