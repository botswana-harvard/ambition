import os

from django.core.wsgi import get_wsgi_application

os.environ.update("ambition.settings.production.reviewer")

application = get_wsgi_application()
