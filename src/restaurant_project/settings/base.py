"""
Django settings for restaurant project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
# reading .env file
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='unsafe-key-please-dont-use-this')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'environ',
    'graphene_django',
    'corsheaders',
    'restaurant_entities.apps.RestaurantEntitiesConfig',
    'graphql_auth',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'restaurant_entities.users',
    'storages',
    'channels',
    'graphene_subscriptions',
]

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restaurant_project.urls'

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

WSGI_APPLICATION = 'restaurant_project.wsgi.application'

ASGI_APPLICATION = "restaurant_project.routing.application"

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

GRAPHENE = {
    'SCHEMA': 'restaurant_graphql.schema.schema',
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
        # 'conference_project.middleware.LoaderMiddleware',
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ]
}

AUTHENTICATION_BACKENDS = [
    "graphql_auth.backends.GraphQLAuthBackend",
    'django.contrib.auth.backends.ModelBackend',
]

GRAPHQL_AUTH = {
    'LOGIN_ALLOWED_FIELDS': ['email'],
    'USER_NODE_EXCLUDE_FIELDS': ["password"],
    # 'REGISTER_MUTATION_FIELDS': {
    #     "email": "String",
    # },
}

GRAPHQL_JWT = {
    'JWT_ALLOW_ANY_CLASSES': [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ResendActivationEmail",
        "graphql_auth.mutations.SendPasswordResetEmail",
        "graphql_auth.mutations.PasswordReset",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.VerifyToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
        "graphql_auth.mutations.VerifySecondaryEmail",
    ],
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
}

AUTH_USER_MODEL = 'users.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Bucharest'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_FROM_EMAIL = 'restaurantubb@gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'restaurantubb@gmail.com'
EMAIL_HOST_PASSWORD = 'zN:+$~mi+apX#YdZ{3f#jSZD'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

# STATICFILES_DIRS = [
#     '/home/cipri/restaurant-backend/static'
# ]
# # STATICFILES_DIRS = [
# #     '/var/app/current/src/restaurant_project/static/'
# # ]

if os.environ.get('DJANGO_DEVELOPMENT', "dev") == "production":
    from .production_settings import *
else:
    from .development_settings import *
