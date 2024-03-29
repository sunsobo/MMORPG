"""
Django settings for MYSITE project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR_OS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-twznexk5zt8$n$$0(2vw%$wyo3&+pvu5q4+fs7)+3e*_2j@th3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_URL = 'test.crmtok.ru'

ALLOWED_HOSTS = [
    '*',
]

ADMINS = [("Admin", "sunsobolev@gmail.com"), ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # apps
    'index',
    'accounts',
    'blog',
    
    # packages
    'ckeditor',
    'ckeditor_uploader',
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

ROOT_URLCONF = 'MYSITE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # apps
                'index.context_processors.index',
            ],
        },
    },
]

WSGI_APPLICATION = 'MYSITE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


MEDIA_URL = 'MYSITE/media/'
MEDIA_PATH = BASE_DIR_OS
MEDIA_ROOT = MEDIA_PATH + '/media/'

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "sunsobolevdev@gmail.com"
EMAIL_HOST_PASSWORD = "kycd xvdi xmps ykcf"
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# SESSIONS
SESSION_COOKIE_AGE = 31536000 # 7209600


# PREPEND_WWW = True

# DJANGO CACHE
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'cache_site/',
        # 'TIMEOUT': 300,  # 0 - cache OFF
        'OPTIONS': {
            'MAX_ENTRIES': 300
        }
    }
}



# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'console_1': {
            'format': '%(asctime)s-12s %(levelname)-4s %(message)s'
        },
        'console_2': {
            'format': '%(asctime)s-12s %(levelname)-8s %(pathname)-4s %(message)s'
        },
        'console_3': {
            'format': '%(asctime)s-12s %(levelname)-8s %(pathname)-4s %(exc_info)-2s %(message)s'
        },


        'file_general': {
            'format': '%(asctime)s %(levelname)-12s %(module)-8s %(message)s'
        },
        'file_errors': {
            'format': '%(asctime)s %(levelname)-12s %(message)-10s %(pathname)-8s %(stack_info)s'
        },
        'file_security': {
            'format': '%(asctime)s %(levelname)-12s %(module)-8s %(message)s'
        },
        'file_email': {
            'format': '%(asctime)s %(levelname)-12s %(message)-8s %(pathname)-s'
        },

    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'handlers': {
        # console
        'console_1': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_1',
        },
        'console_2': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_2',
        },
        'console_3': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_3',
        },
        'console_4': {
            'level': 'CRITICAL',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_3',
        },

        # general
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'file_general',
            'filename': BASE_DIR / './_general.log_'
        },


        # errors
        'file_errors_1': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'file_errors',
            'filename': BASE_DIR / './_errors.log_'
        },
        'file_errors_2': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'formatter': 'file_errors',
            'filename': BASE_DIR / './_errors.log_'
        },


        # security
        'file_security': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file_security',
            'filename': BASE_DIR / './_security.log_'
        },


        'mail_admins': {
            'level': 'ERROR',
            # отправка только, когда DEBUG=False
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'file_email',
            'include_html': True,
        },
    },

    'loggers': {
        # general
        'django': {
            'level': 'DEBUG',
            'handlers': [
                'console_1',
                'console_2',
                'console_3',
                'console_4',
                'file_general'
            ],
        },


        # errors
        'django.request': {
            'level': 'DEBUG',
            'handlers': [
                'file_errors_1', 
                'file_errors_2', 
                'mail_admins'
            ],
        },
        'django.server': {
            'level': 'DEBUG',
            'handlers': [
                'file_errors_1', 
                'file_errors_2', 
                'mail_admins'
            ],
        },
        'django.template': {
            'level': 'DEBUG',
            'handlers': [
                'file_errors_1', 
                'file_errors_2'
            ],
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': [
                'file_errors_1', 
                'file_errors_2'
            ],
        },


        # security
        'django.security': {
            'level': 'DEBUG',
            'handlers': [
                'file_security'
            ],
        },
    },
}





# django-ckeditor
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Full': [
            ['Blockquote', 'Format',],
            ['Bold', 'Italic', 'Underline', 'Strike' ],
            ['NumberedList', 'BulletedList', ],
            ['Smiley', 'TextColor', 'HorizontalRule' ],
            [ 'Link', 'Image', 'Youtube' ],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight' ],
        ],
        'height': 500,
        'width' : '100%',
        'allowedContent': True,
        'extraPlugins' : 'youtube',
        'config.enterMode' : 'CKEDITOR.ENTER_BR',
    },
    
}

# CKEDITOR


CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True
