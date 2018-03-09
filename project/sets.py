# Standard Libary
import os

from cryptography import x509
from cryptography.hazmat.backends import default_backend


# Third-Party
import dj_database_url

# Django
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        var = os.environ[var_name]
        # Replace unix strings with Python Booleans
        if var == 'True':
            var = True
        if var == 'False':
            var = False
    except KeyError:
        error_msg = "Set the {var_name} env var".format(var_name=var_name)
        raise ImproperlyConfigured(error_msg)
    return var


# Core
DEBUG = get_env_variable("DEBUG")
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SECRET_KEY = get_env_variable("SECRET_KEY")
DEFAULT_FROM_EMAIL = "admin@barberscore.com"
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
USE_I18N = False
USE_L10N = False
APPEND_SLASH = False
ALLOWED_HOSTS = [
    'localhost',
    'testserver',
    '*.herokuapp.com',
    '*.barberscore.com',
]

# Datetime
TIME_ZONE = 'US/Pacific'
USE_TZ = True
DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'H:i:s'
DATETIME_FORMAT = 'Y-m-d H:i:s'

# Authentication
AUTH_USER_MODEL = "api.User"
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
USERNAME_FIELD = 'email'
REQUIRED_FIELDS = []
LOGIN_URL = 'admin:login'
LOGIN_REDIRECT_URL = 'admin:index'
LOGOUT_REDIRECT_URL = 'admin:login'

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Templating
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
            ],
        }
    },
]

# Database
DATABASES = {
    'default': dj_database_url.parse(
        get_env_variable("DATABASE_URL"),
        conn_max_age=600,
    ),
    'bhs_db': dj_database_url.parse(
        get_env_variable("BHS_DATABASE_URL"),
        conn_max_age=600,
    )
}
DATABASE_ROUTERS = [
    'routers.BHSRouter',
]


# Caches
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": get_env_variable("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": int(get_env_variable("REDIS_MAX_CONNECTIONS")),
            },
        }
    },
}

# Sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# RQ
RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'default',
        'ASYNC': get_env_variable("RQ_ASYNC"),
    },
    'high': {
        'USE_REDIS_CACHE': 'default',
        'ASYNC': get_env_variable("RQ_ASYNC"),
    },
}
RQ_SHOW_ADMIN_LINK = True

# File Management
# Staticfiles
CLOUDINARY_URL = get_env_variable("CLOUDINARY_URL")
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Rest Framework (JSONAPI)
REST_FRAMEWORK = {
    'PAGE_SIZE': 100,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_json_api.pagination.PageNumberPagination',
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework_json_api.renderers.JSONRenderer',
        'rest_framework.renderers.JSONRenderer',
        'api.renderers.NoHTMLFormBrowsableAPIRenderer',
        'rest_framework.renderers.AdminRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

# Email
EMAIL_BACKEND = get_env_variable("EMAIL_BACKEND")
EMAIL_PORT = get_env_variable("EMAIL_PORT")

# JSONAPI
JSON_API_FORMAT_KEYS = 'dasherize'
JSON_API_FORMAT_TYPES = 'dasherize'
JSON_API_PLURALIZE_TYPES = False
APPEND_TRAILING_SLASH = False

# Sentry
RAVEN_CONFIG = {
    'environment': get_env_variable("ENVIRONMENT"),
    'dsn': get_env_variable("SENTRY_DSN"),
    # 'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}

# Auth0
AUTH0_CLIENT_ID = get_env_variable("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = get_env_variable("AUTH0_CLIENT_SECRET")
AUTH0_DOMAIN = get_env_variable("AUTH0_DOMAIN")
AUTH0_API_ID = get_env_variable("AUTH0_API_ID")
AUTH0_API_SECRET = get_env_variable("AUTH0_API_SECRET")
AUTH0_AUDIENCE = get_env_variable("AUTH0_AUDIENCE")


def jwt_get_username_from_payload_handler(payload):
    """Switch to email as JWT username payload."""
    return payload.get('email')


cert = get_env_variable("AUTH0_CERTIFICATE")
pem_data = cert.encode()
cert = x509.load_pem_x509_certificate(pem_data, default_backend())
jwt_public_key = cert.public_key()

JWT_AUTH = {
    'JWT_AUDIENCE': AUTH0_CLIENT_ID,
    'JWT_PAYLOAD_GET_USERNAME_HANDLER': jwt_get_username_from_payload_handler,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_PUBLIC_KEY': jwt_public_key,
    'JWT_ALGORITHM': 'RS256',
}


# Algolia
ALGOLIA = {
    'APPLICATION_ID': get_env_variable("ALGOLIASEARCH_APPLICATION_ID"),
    'API_KEY': get_env_variable("ALGOLIASEARCH_API_KEY"),
    'AUTO_INDEXING': get_env_variable("ALGOLIASEARCH_AUTO_INDEXING"),
    'INDEX_SUFFIX': get_env_variable("ALGOLIASEARCH_INDEX_SUFFIX"),
}

# Applications
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'cloudinary_storage',
    'cloudinary',
    'rest_framework',
    'django_filters',
    'dry_rest_permissions',
    'django_rq',
    'django_fsm',
    'django_fsm_log',
    'fsm_admin',
    'algoliasearch_django',
    'raven.contrib.django.raven_compat',
    'api',
    'bhs',
]

ENVIRONMENT = get_env_variable("ENVIRONMENT")

if ENVIRONMENT == 'dev':
    # Debug Toolbar
    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'loggers': {
            'api': {
                'handlers': [
                    'console',
                ],
                'level': 'DEBUG',
            },
            'importer': {
                'handlers': [
                    'console',
                    'logfile',
                ],
                'level': 'DEBUG',
            },
            'updater': {
                'level': 'DEBUG',
                'handlers': [
                    'console',
                ],
            },
            'console': {
                'level': 'DEBUG',
                'handlers': [
                    'console',
                ],
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'logfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BASE_DIR, 'dev.log'),
                'maxBytes': 5000000,
                'backupCount': 10,
                'formatter': 'standard',
            },
        },
        'formatters': {
            'simple': {
                'format': '%(levelname)s %(message)s',
            },
            'standard': {
                'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
        },
    }

    INSTALLED_APPS += [
        'debug_toolbar',
        'whitenoise.runserver_nostatic',
    ]

elif ENVIRONMENT == 'staging':
    # Heroku
    # SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # SECURE_SSL_REDIRECT = True
    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'loggers': {
            'api': {
                'handlers': [
                    'console',
                ],
                'level': 'INFO',
            },
            'importer': {
                'handlers': [
                    'console',
                ],
                'level': 'INFO',
            },
            'updater': {
                'handlers': [
                    'console',
                ],
                'level': 'INFO',
            },
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': [
                    'console'
                ],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': [
                    'console'
                ],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': [
                    'console'
                ],
                'propagate': False,
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
            },
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                'tags': {'custom-tag': 'x'},
            },
        },
    }

elif ENVIRONMENT == 'prod':
    SENDGRID_API_KEY = get_env_variable("SENDGRID_API_KEY")
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'loggers': {
            'api': {
                'handlers': [
                    'console',
                ],
                'level': 'INFO',
            },
            'importer': {
                'handlers': [
                    'console',
                ],
                'level': 'INFO',
            },
            'updater': {
                'handlers': [
                    'console',
                ],
                'level': 'INFO',
            },
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': [
                    'console'
                ],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': [
                    'console'
                ],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': [
                    'console'
                ],
                'propagate': False,
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
            },
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                'tags': {'custom-tag': 'x'},
            },
        },
    }
else:
    error_msg = "No settings for {0}.".format(ENVIRONMENT)
    raise ImproperlyConfigured(error_msg)