# -*- coding: utf-8 -*-
import os
import dj_database_url

gettext = lambda s: s
PROJECT_ROOT = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

DEBUG = bool(os.environ.get('DEBUG', False))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

INTERNAL_IPS = os.environ.get('INTERNAL_IPS', '127.0.0.1').split()

SQLITE_DB_URL = 'sqlite:///' + os.path.join(PROJECT_ROOT, 'sqlite3.db')

DATABASES = {'default': dj_database_url.config(default=SQLITE_DB_URL)}

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()

EMAIL_BACKEND = ('django.core.mail.backends.%s.EmailBackend' %
                 os.environ.get('EMAIL_BACKEND_MODULE', 'console'))

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = bool(os.environ.get('EMAIL_USE_TLS', False))
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'project', 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

if DEBUG:
    MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

LOCALE_PATHS = [
    os.path.join(PROJECT_ROOT, 'locale')
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'project.core.context_processors.cache_timeout',
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

INSTALLED_APPS = [
    'admin_shortcuts',
    'djangocms_admin_style',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.admin',

    # cms plugins
    'djangocms_text_ckeditor',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_snippet',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    # external    
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'reversion',
    'easy_thumbnails',
    'storages',
    'robots',
    'compressor',
]

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']

SENTRY_DSN = os.environ.get('SENTRY_DSN')

if SENTRY_DSN:
    INSTALLED_APPS += ['raven.contrib.django.raven_compat']
    RAVEN_CONFIG = {'dsn': SENTRY_DSN}

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# django admin shortcuts
ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url': '/',
                'open_new_window': True,
            },
            {
                'url_name': 'admin:cms_page_changelist',
                'title': gettext('Pages'),
            },
            {
                'url_name': 'admin:filer_folder_changelist',
                'title': gettext('Files'),
            },
            {
                'url_name': 'admin:auth_user_changelist',
                'title': gettext('Users'),
            },
        ],
    },
]

LANGUAGES = [
    ('en', gettext('English')),
    ('pl', gettext('Polish')),
]

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': gettext('English'),
            'fallbacks': [],
        },
        {
            'code': 'pl',
            'name': gettext('Polish'),
            'fallbacks': [],
        },

    ],
    'default': {
        'fallbacks': [],
        'redirect_on_fallback': False,
        'public': True,
        'hide_untranslated': True,
    }
}

CMS_TEMPLATES = (
    ('fullwidth.html', 'Full-width template'),
    ('sidebar_left.html', 'Sidebar left template'),
    ('homepage.html', 'Homepage template'),
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

COMPRESS_ENABLED = bool(os.environ.get('COMPRESS_ENABLED', False))
COMPRESS_OUTPUT_DIR = ''
COMPRESS_ROOT = STATIC_ROOT

# Amazon S3 configuration
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SECURE_URLS = bool(os.environ.get('AWS_S3_SECURE_URLS', False))
AWS_QUERYSTRING_AUTH = bool(os.environ.get('AWS_QUERYSTRING_AUTH', False))

if AWS_STORAGE_BUCKET_NAME:
    DEFAULT_FILE_STORAGE = 'project.core.s3.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'project.core.s3.StaticRootS3BotoStorage'
    THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

    S3_URL = '//%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL + STATIC_URL
    MEDIA_URL = S3_URL + MEDIA_URL

    if COMPRESS_ENABLED:
        COMPRESS_STORAGE = 'project.core.s3.CachedS3BotoStorage'
        COMPRESS_URL = STATIC_URL
        STATICFILES_STORAGE = COMPRESS_STORAGE

MEMCACHE_SERVERS = os.environ.get('MEMCACHE_SERVERS')

if MEMCACHE_SERVERS:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': MEMCACHE_SERVERS,
        }
    }
