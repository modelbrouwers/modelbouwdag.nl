import os

from .base import *

#
# Standard Django settings.
#

DEBUG = False
WSGI_APPLICATION = 'modelbouwdag.wsgi.default.application'
ENVIRONMENT = 'production'
SHOW_ALERT = False

ADMINS = (
    ('Sergei Maertens', 'sergei@modelbrouwers.nl'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('SECRET_KEY')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'live.modelbouwdag.nl',
    'modelbouwdag.nl',
]

# Memcached cache backend setup.
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

# Caching templates.
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', RAW_TEMPLATE_LOADERS),
]

# Caching sessions.
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Production logging facility.
LOGGING['loggers'].update({
    'modelbouwdag': {
        'handlers': ['project'],
        'level': 'WARNING',
        'propagate': True,
    },
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})

#
# django-maintenancemode
#
MAINTENANCE_MODE = False

#
# Raven
#
INSTALLED_APPS = INSTALLED_APPS + [
    'raven.contrib.django.raven_compat',
]
RAVEN_CONFIG = {
    'dsn': os.getenv('RAVEN_DSN'),
}
