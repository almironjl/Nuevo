# context_processors.py context_processors
from django.conf import settings

def admin_media_prefix(request):
    return {'ADMIN_MEDIA_PREFIX': '<STATIC_URL>/admin/' }