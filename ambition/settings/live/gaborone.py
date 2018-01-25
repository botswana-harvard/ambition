from ...sites import get_site_id
from .base_live import *

# for django.contrib.sites
SITE_ID = get_site_id('gaborone')

WSGI_APPLICATION = 'ambition.wsgi.gaborone.application'
