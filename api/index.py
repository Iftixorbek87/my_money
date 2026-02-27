import os
import sys
from django.core.wsgi import get_wsgi_application

# Backend papkasini sys.path ga qo'shamiz
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

# Vercel uchun settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.vercel_settings')

# WSGI application ni olamiz
application = get_wsgi_application()

# Vercel serverless uchun to'g'ri handler
def handler(environ, start_response):
    return application(environ, start_response)
