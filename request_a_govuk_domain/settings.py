"""
Django settings for request_a_govuk_domain project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import re
import logging
import uuid
from pathlib import Path
from environ import Env

env = Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

Env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: bool = env.bool("DEBUG", default=False)
if DEBUG:
    # Use dotenv for debug environments
    from dotenv import load_dotenv

    load_dotenv()

SECRET_KEY: str = (
    str(uuid.uuid4()) if DEBUG else env.str("SECRET_KEY", default="not_set")
)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
ENVIRONMENT = env.str("ENVIRONMENT", default=None)

# AWS related settings
IS_AWS: bool = env.bool("IS_AWS", default=False)
IS_SCANNING_ENABLED: bool = env.bool("SCANNING_ENABLED", default=True)
AWS_STORAGE_BUCKET_NAME = env.str(
    "S3_MEDIA_ROOT", default=f"registration-app-media-root-{ENVIRONMENT}"
)

# Application definition

INSTALLED_APPS = [
    "request_a_govuk_domain.request",
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "psqlextra",
    "govuk_frontend_django",
    "crispy_forms",
    "crispy_forms_gds",
    "simple_history",
    "phonenumber_field",
    "storages",
    "django_celery_results",
    "gdstorage",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = ["gds"]
CRISPY_TEMPLATE_PACK = "gds"

MIDDLEWARE = [
    "csp.middleware.CSPMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

X_FRAME_OPTIONS = "SAMEORIGIN"

FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]

ROOT_URLCONF = "request_a_govuk_domain.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "libraries": {
                "csp": "csp.templatetags.csp",
            },
            "context_processors": [
                "csp.context_processors.nonce",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "request_a_govuk_domain.request.utils.variable_page_content",
            ],
        },
    },
]

WSGI_APPLICATION = "request_a_govuk_domain.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if "RDS_DB_NAME" in os.environ:
    DATABASES = {
        "default": {
            "ENGINE": "psqlextra.backend",
            "NAME": os.environ["RDS_DB_NAME"],
            "USER": os.environ["RDS_USERNAME"],
            "PASSWORD": os.environ["RDS_PASSWORD"],
            "HOST": os.environ["RDS_HOST"],
            "PORT": os.environ["RDS_PORT"],
            "OPTIONS": {
                "connect_timeout": 5,
            },
        }
    }
else:
    DATABASES = {
        "default": env.db_url(
            default="postgresql:///govuk_domain", engine="psqlextra.backend"
        ),
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Logging
"""The logging configuration for the application.

See :external+django:ref:`configuring-logging` for more information.
"""
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] [%(process)d:%(threadName)s] [%(levelname)s] [%(name)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S %z",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "": {
            "level": ("INFO" if not DEBUG else "DEBUG"),
            "handlers": ["console"],
            "propagate": True,
        },
        "django": {
            # remove the console handler from this level as it is already attached at the root level.
            "handlers": ["mail_admins"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# Django Whitenoise Configuration
WHITENOISE_SKIP_COMPRESS_EXTENSIONS = [".map"]
WHITENOISE_ALLOW_ALL_ORIGINS = False
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# https://djangosnippets.org/snippets/1303/
CONTENT_TYPES = ["png", "jpeg", "jpg", "pdf"]
# 10 MB
MAX_UPLOAD_SIZE = "10485760"

CLAMD_TCP_ADDR = env.str(
    "CLAMD_TCP_ADDR", default="clamav.internal-domains-registry-cluster"
)
CLAMD_TCP_SOCKET = 3310

# Cross-site request forgery protection
# What: https://owasp.org/www-community/attacks/csrf
# How: https://docs.djangoproject.com/en/5.0/ref/settings/
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    CSRF_TRUSTED_ORIGINS = [f"https://{os.environ.get('DOMAIN_NAME', 'localhost')}"]
    CSRF_FAILURE_VIEW = "request_a_govuk_domain.request.views.csrf_failure_view"
    SESSION_COOKIE_SECURE = True

# Set session (end-user or admin) to expire in 24 hours
SESSION_COOKIE_AGE = 24 * 60 * 60

# Content Security Policy: only allow images, stylesheets and scripts from the
# same origin as the HTML
CSP_IMG_SRC = "'self'"
CSP_STYLE_SRC = "'self' 'unsafe-inline'"
CSP_SCRIPT_SRC = "'self' https://*.googletagmanager.com"
CSP_CONNECT_SRC = "'self' https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com"
CSP_FRAME_SRC = "'self' https://www.googletagmanager.com"
CSP_FORM_ACTION = "'self'"
CSP_FRAME_ANCESTORS = "'self'"
CSP_INCLUDE_NONCE_IN = ["script-src", "img-src", "connect-src", "frame-src"]
# Disable CSP for debug as it prevent the style sheets from loading on  localhost
CSP_REPORT_ONLY = False

# HTTP Strict Transport Security settings
# Tell browsers to only use HTTPS for a year
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # We don't have subdomains but it doesn't hurt
SECURE_HSTS_PRELOAD = True  # Tell browsers to remember HTTPS only

# Sentry monitoring
SENTRY_DSN = env.str("SENTRY_DSN", default=None)
if SENTRY_DSN is not None:
    import sentry_sdk

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        enable_tracing=True,
        environment=ENVIRONMENT,
    )

# Only enable S3 storage if it is explicitly enabled or on AWS
S3_STORAGE_ENABLED = env.bool("S3_STORAGE_ENABLED", default=IS_AWS)

CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", "redis://localhost/0")
CELERY_RESULT_BACKEND = "django-db"
CELERY_TASK_DEFAULT_QUEUE = env.str("QUEUE_NAME", "celery")
CELERY_BEAT_SCHEDULE_FILENAME = env.str(
    "CELERY_BEAT_SCHEDULE_FILENAME", default="celerybeat-schedule"
)
CELERY_BROKER_TRANSPORT_OPTIONS = env.json("CELERY_BROKER_TRANSPORT_OPTIONS", {})
# The setting "CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True" is to get rid of the following deprecation warning
# message, which shows up in the Cloudwatch Celery worker logs
#
# PendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
# whether broker connection retries are made during startup in Celery 6.0 and above. If you wish to retain the
# existing behavior for retrying connections on startup, you should set broker_connection_retry_on_startup to True.
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

# Apply the filter only if we are running under the Gunicorn server on AWS.
#   - We use Gunicon server when the application is deployed on AWS
#   - We only get these type of requests (health check probes) only on AWS
is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
if is_gunicorn:

    class LbCheckFilter(logging.Filter):
        """
        filter out loadbalancer successful check respnse.
        This is needed to reduce the log entries in our application log
        """

        expression = re.compile(r'.*?GET / HTTP/1.1" 200.*?ELB-HealthChecker/2.0.*')

        def filter(self, record):
            return not self.expression.match(record.getMessage())

    gunicorn_logger = logging.getLogger("gunicorn.access")
    current_filters = gunicorn_logger.filters
    add_filter = True
    if current_filters:
        # Make sure we do not add the filter multiple times
        for filter in current_filters:
            if type(filter) is LbCheckFilter:
                add_filter = False
    if add_filter:
        gunicorn_logger.addFilter(LbCheckFilter())

# Google Drive Storage Settings
GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = os.path.join(
    BASE_DIR, "request", "keys", "testduetai-408211-3f148c94507c.json"
)
