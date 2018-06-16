"""
Django settings for max7p project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&yhv=ikyfdgb6q6d-=qitik!ht&k*azqsdk%9u0@@p)d363ph*'

# LOGIN_REDIRECT_URL = '/users/home'

PAGINATION_COUNT = 5

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# AUTH_USER_MODEL = 'users.ExtendedUser'

BASE_URL='192.168.0.27:9001'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'post_office',
    'owner',
    'search',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rental.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'user_dashboard.context_processors.user_detail',
                # 'activities.context_processors.get_company_id',
            ],
        },
    },
]

WSGI_APPLICATION = 'rental.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rental',
        'USER': 'root',
        'PASSWORD': 'M4ster@809',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

DATE_INPUT_FORMATS = ('%d-%m-%Y')

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

POST_OFFICE = {
    'DEFAULT_PRIORITY' : 'now'
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "dhanesh@esferasoft.com"
EMAIL_PORT = 587  # default smtp port
EMAIL_HOST_PASSWORD = "dhanesh_esfera"
EMAIL_USE_TLS = True
# Sending email detail
# EMAIL_ADDRESS = "itsmepython21@gmail.com"
# PASSWORD = "esfera0143"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILE_DIR=(os.path.join(BASE_DIR, 'static/'))
MEDIA_URL = '/media/'
# MEDIA_ROOT = '/home/ip-d/Documents/parul/projects/Max7p/max7p/media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CHROMEDRIVER_PATH='/home/tarun/Documents/inhouse/rental/chromedriver'
GEOIP_PATH ='GeoLiteCity.dat'
