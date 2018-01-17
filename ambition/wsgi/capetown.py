import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("ambition.settings.production.capetown")

application = get_wsgi_application()
