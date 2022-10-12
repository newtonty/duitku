"""
WSGI config for duitku project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(Path(__file__).parent.parent, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duitku.settings')

application = get_wsgi_application()
