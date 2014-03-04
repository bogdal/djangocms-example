from django.conf import settings


def cache_timeout(request):
    timeout = settings.CACHE_MIDDLEWARE_SECONDS
    if request.user.is_superuser:
        timeout = 0
    return {'CACHE_TIMEOUT': timeout}
