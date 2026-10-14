from .base import *

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]  # fast tests
CELERY_TASK_ALWAYS_EAGER = True  # tasks run inline in tests