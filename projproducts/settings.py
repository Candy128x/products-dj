"""
Django settings for projproducts project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from decouple import config, Config, RepositoryEnv
from pathlib import Path
import logging
import logging.config, os

# env = 'dev'
env = 'prod'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-whty&kdm971_*xk2mz0wf4_9q9(92_#+qz6=lfc(&-ivxnnjvg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'products-dj-v5.herokuapp.com']
# ALLOWED_HOSTS = ['*']

env_config = Config(RepositoryEnv(f'.env_{env}'))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_crontab',
    'import_export',

    # Custom App
    'products',
    'home'
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

ROOT_URLCONF = 'projproducts.urls'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
# # Find templates in the same folder as settings.py.
# TEMPLATE_DIRS = (
#     os.path.join(SETTINGS_PATH, 'templates'),
# )

WSGI_APPLICATION = 'projproducts.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CRONJOBS = [
    # ('*/1 * * * *', 'home.cron_jobs.send_email_cron_job.send_email'),
    ('* 6 * * *', 'home.cron_jobs.send_email_cron_job.send_email')
]

IMPORT_EXPORT_IMPORT_PERMISSION_CODE = 'delete'
IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'delete'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env_config('EMAIL_HOST_USER')  #sender's email-id
EMAIL_HOST_PASSWORD = env_config('EMAIL_HOST_PASSWORD')  #password associated with above email-id
EMAIL_BCC = env_config('EMAIL_BCC').split(',')

SEND_EMAIL_API_SALT_KEY = ['57fef2e83b67478972e611318bd7fc76edcfe5f5']

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Logger
if env == 'prod':
    SET_LOGGER_LEVEL = 'ERROR'
else:
    SET_LOGGER_LEVEL = 'DEBUG'
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # 'format': '%(name)-12s %(levelname)-8s %(message)s'
            'format': '\n[%(asctime)s] %(levelname)s - %(name)s - file: %(module)s - fun: %(funcName)s() - LN: %(lineno)d \n%(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': SET_LOGGER_LEVEL,
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': '/tmp/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': SET_LOGGER_LEVEL,
            'handlers': ['console', 'file']
        }
    }
})


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

MEDIA_URL = '/'
MEDIA_ROOL = os.path.join(BASE_DIR, '')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
