"""
Django settings for airbnb_project project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import environ
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("this is the base directory: " + BASE_DIR) #/Users/stateofplace/new_codes/airbnb_project_folder/airbnb_project_container

env = environ.Env()
# env = environ.Env.read_env() #not needed?
# env = environ.Env.read_env(env_file=os.path.join(BASE_DIR, '/airbnb_project/.env')) #doesn't work it's none... might help us with env thing later 
# print(env)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#produciton security issue, should be 
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['80','localhost','.airbnb-policy-tool.herokuapp.com','127.0.0.1:8080/', 'http://127.0.0.1:8000/']
#     'http://127.0.0.1:8000/',
#     'http://127.0.0.1:8080/',
#     '127.0.0.1:8080/',
#     '127.0.0.1:8000/',
#   '127.0.0.1',
#   '111.222.333.444',
#   'http://airbnb-policy-tool.herokuapp.com/',
#   'www.airbnb-policy-tool.herokuapp.com',
#   '.airbnb-policy-tool.herokuapp.com',
#   'https://airbnb-policy-tool.herokuapp.com/']

#why is this not being picked up on? I think I set it with export so it doesn't care... so not workign from env file? 
#should be os.environ['SECRET_KEY'] like others ... TODO  https://django-environ.readthedocs.io/en/latest/quickstart.html and https://stackoverflow.com/questions/52700257/django-2-not-able-to-load-env-variables-from-the-env-file-to-setting-py-file https://stackoverflow.com/questions/70518296/heroku-python-local-environment-variables
SECRET_KEY = env('SECRET_KEY') #os.environ['SECRET_KEY']
# Application definition
#production things
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CONN_MAX_AGE = None
CONN_HEALTH_CHECKS=True
#true in production
SECURE_SSL_REDIRECT=True


INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'csvimport.app.CSVImportConf',
    'airbnb_app.apps.AirbnbAppConfig',
    # 'airbnb_app',
    'django.contrib.gis',
    'environ', #unsure... why not working
    'django_distill',
]

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

ROOT_URLCONF = 'airbnb_project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'airbnb_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', 
        'NAME': env('NAME'), #os.environ['NAME'], #(env('NAME'), #database name
        'USER': env('USER'), #os.environ['USER'], #env('USER'),
        'PASSWORD': env('PASSWORD'), #os.environ['PASSWORD'],#env('PASSWORD'), #'d3f34ed8cec0b7d96956ab2ba931439ee7daa7a4c9f88ab67135883038c6',
        'HOST': 'localhost', #env('localhost'),didn't work... 
        'PORT': '5432',
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis'
        # 'NAME': 'df285fnf6qoujc', Doesn't seem to work, this is heroku name of databse... 
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR + '/staticfiles'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configure Django App for Heroku.
import django_heroku #django_on_heroku #or import django_heroku
django_heroku.settings(locals()) #django_on_heroku.settings(locals())

# i might need the below... for postgis error ... but it causes envir var errors 
import dj_database_url
DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
DATABASES['default']['NAME'] = os.environ['NAME']
