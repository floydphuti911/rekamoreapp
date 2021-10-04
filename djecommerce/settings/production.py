# from .base import *
from decouple import config

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['ip-address', 'rekamore.herokuapp.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('floyddipela'),
        'USER': config('floydflava'),
        'PASSWORD': config('Floydfuckme-6'),
        'HOST': config('127.0.0.1'),
        'PORT': '5432'
    }
}

STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
