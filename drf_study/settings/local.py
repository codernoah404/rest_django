from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=!hcgfr%fr#iz8llkv@f$&^e03+u&lc9)48+loqox^7+%h&m!b"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

INSTALLED_APPS += [
    'study.apps.StudyConfig'
]