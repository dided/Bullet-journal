# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Templates path
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

# Templates dir
TEMPLATE_DIRS = (
    TEMPLATE_PATH,        
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATIC_PATH = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,       
)

FIXTURE_PATH = os.path.join(BASE_DIR, 'fixtures')

FIXTURE_DIRS = (
    FIXTURE_PATH,       
)

# Redirect urls
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/app/'

# No trailing slash
APPEND_SLASH = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'whv$&96%jbjl^%r=x&6*5s#=s391ln^9#wb0b2e6z195uwqzep'

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'south',
    'django_extensions',
    'registration',
    'bootstrap3',
    'jquery',
    'djangular',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bullet.urls'

WSGI_APPLICATION = 'bullet.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
    }
}

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

try:
    from local_settings import *
except Exception as e: 
    pass

