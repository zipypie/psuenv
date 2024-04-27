"""
WSGI config for projectsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/jubnick/psuenv/PSUSphere/projectsite'  # Path to manage.py

if path  not in sys.path:
        sys.path.insert(0,path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'projectsite.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())
