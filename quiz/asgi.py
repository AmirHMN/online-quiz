"""
ASGI config for quiz project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import dotenv
from django.core.asgi import get_asgi_application

dotenv.read_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings.dev')

application = get_asgi_application()
