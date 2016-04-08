from .base import *

#
# Standard Django settings.
#

DEBUG = False
WSGI_APPLICATION = 'modelbouwdag.wsgi.production.application'
ENVIRONMENT = 'production'
SHOW_ALERT = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'modelbouwdag',
        'USER': 'modelbouwdag',
        'PASSWORD': 'modelbouwdag',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!v-lk&if2tza$-mrmr+st3$g=!mous4!+-!ked^pkuurj^o)th'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

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
    'dsn': 'http://',
}
