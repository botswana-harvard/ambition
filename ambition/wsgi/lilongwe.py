import os

from django.core.wsgi import get_wsgi_application

os.environ.update("ambition.settings.production.lilongwe")

application = get_wsgi_application()
