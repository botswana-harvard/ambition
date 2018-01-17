import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("ambition.settings.uat")

application = get_wsgi_application()
