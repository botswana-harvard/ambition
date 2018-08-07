from ...sites import get_site_id
from .base_live import *

# for django.contrib.sites
SITE_ID = get_site_id('mbarara')

WSGI_APPLICATION = 'ambition.wsgi.mbarara.application'

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'mbarara.ambition.bhp.org.bw']

TIME_ZONE = 'Africa/Mbarara'
