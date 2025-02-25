"""
Django settings for creactivaweb project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
import mimetypes


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = 'https://www.creactivaanimaciones.cl/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# VER SI HAY QUE AGREGAR MÁS HOSTS A ESTA CONFIGURACIÓN
ALLOWED_HOSTS = ['www.creactivaanimaciones.cl/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'main',
    'cursos',
    'suscripciones',
    'dashboards'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'creactivaweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'creactivaweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'
# America/Santiago
USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    '/home/creacti3/creactivaweb/static'
]

STATIC_ROOT = '/home/creacti3/public_html/static/'



#Whitenoise Middleware para manejo de archivos estáticos
# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }
WHITENOISE_INDEX_FILE = True

#Whitenoise Middleware para manejo de archivos estáticos
# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }
WHITENOISE_INDEX_FILE = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Variables para almacenar redireccionamientos al hacer login o logout
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# SSL
#SECURE_SSL_REDIRECT = True

# algo sobre middleware para iFrames
X_FRAME_OPTIONS = "SAMEORIGIN"

# MIME types
#mimetypes.add_type("text/html", ".js", True)

# django setting.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

# MAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.creactivaanimaciones.cl'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = '_mainaccount@creactivaanimaciones.cl'
EMAIL_HOST_PASSWORD = 'GA,B%L7p8JB)#vN^'
EMAIL_TIMEOUT = 20
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# WEBPAY
WEBPAY_URL = 'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions'
WEBPAY_ID = '597055555532'
WEBPAY_SECRET = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'

USE_THOUSAND_SEPARATOR = True
USE_DECIMAL_SEPARATOR = False
NUMBER_GROUPING = 3
THOUSAND_SEPARATOR = "."

# JWT PASS
JWT_SECURE = "=)^+ls6f^[mb"
# LOG DE ERRORES
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}