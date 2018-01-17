"""
Default wsgi for tests and local runserver or single app instance
setup for uat.

If uat, first export the environment variable

    export DJANGO_SETTINGS_MODULE=ambition.settings.uat

"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ambition.settings")

application = get_wsgi_application()
