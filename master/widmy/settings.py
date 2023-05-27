"""
Django settings for widmy project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eo#&=eao_tv4cx5i0*w28i&b)zyl0+oe!fr8pd^!6e%#s(*+%5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'historiasClinicas',
    'pacientes',
    'adendas',
    'social_django',
    'dj_cqrs',
    #'widmy',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'widmy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'widmy', 'templates')],
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

WSGI_APPLICATION = 'widmy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#PostgresSQL database
# DATABASES = {
#      "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "widmydb",
#         "USER": "widmy_user",
#         "PASSWORD": "widmy1",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }
# DATABASES = {
#      "default": {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         "NAME": "widmy2",
#         "USER": "jalfonsor",
#         "PASSWORD": "Mundo753",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

DATABASES = {
      "default": {
         "ENGINE": "django.db.backends.postgresql_psycopg2",
         "NAME": "master-db",
         "USER": "master-user",
         "PASSWORD": "widmy2503",
         "HOST": "10.102.64.3", #El de la SQL Postgres en GCP
         "PORT": "5432",
     }
 }



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static', 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "https://widmy-g3.us.auth0.com/v2/logout?returnTo=http%3A%2F%2F34.31.107.182:8080"



SOCIAL_AUTH_TRAILING_SLASH = False # Remove end slash from routes 
SOCIAL_AUTH_AUTH0_DOMAIN = 'widmy-g3.us.auth0.com' 
SOCIAL_AUTH_AUTH0_KEY = 'GjfQ9O2W7Ge4iBzGxvROMphw3g7GQkJ4' 
SOCIAL_AUTH_AUTH0_SECRET = 'T-8LUrt888c0KFh7vJgtoFu3xmb94GsnkREbETxIDASLt4oejIR9Dqnn3Jdm991h' 
SOCIAL_AUTH_AUTH0_SCOPE = [ 
    'openid', 
    'profile',
    'email',
    'role', 
    ] 

AUTHENTICATION_BACKENDS = { 
    'widmy.auth0backend.Auth0', 
    'django.contrib.auth.backends.ModelBackend', 
    }


# CQRS settings
CQRS = {
    'transport': 'dj_cqrs.transport.RabbitMQTransport',
    'host': '10.128.0.8',
    'port': 5672,
    'user': 'widmy-app',
    'password': 'widmy2503',
}