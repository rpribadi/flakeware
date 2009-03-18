# Django settings for cs project.

import sys
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    ('Riki Pribadi', 'riki.pribadi@yahoo.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.

#LOCALHOST
#DATABASE_NAME = 'flakeware'             # Or path to database file if using sqlite3.
#DATABASE_USER = 'root'             # Not used with sqlite3.
#DATABASE_PASSWORD = 'root'         # Not used with sqlite3.

#FLAKEWARE.COM
DATABASE_NAME = 'rpribadi_fw'             # Or path to database file if using sqlite3.
DATABASE_USER = 'rpribadi_fw'             # Not used with sqlite3.
DATABASE_PASSWORD = 'b1a7aefa'         # Not used with sqlite3.

DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media.flakeware.com/media/'
#MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://media.flakeware.com/admin/'
#ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bzss94+g%(ue(l8xj57w123jftro1qo_-xhbb_aqv%2=wc96ok'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS =("django.core.context_processors.auth",
                              "django.core.context_processors.media",
                              'django.core.context_processors.request',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'flakeware.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.flatpages',
    
    'django.contrib.markup',
    'django.contrib.comments',
    'tagging',
    'flatpages',
    'sorl.thumbnail',
    'filebrowser',
    'gravatar',
    'project',
    'book',
    'tinymce',
    'compress',
    'basic.blog',
    'basic.bookmarks',
    
)

COMPRESS = True
COMPRESS_AUTO = True
COMPRESS_VERSION = True

THUMBNAIL_SUBDIR = 'cache'


COMPRESS_CSS = {
    'main_css': {
        'source_filenames': (
                             'css/main.css', 
                            ),
        'output_filename': 'css/main_compressed.r?.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'syntaxhighlighter_css': {
        'source_filenames': (
                             'css/syntaxhighlighter/styles/shCore.css', 
                             'css/syntaxhighlighter/styles/shThemeDefault.css'
                            ),
        'output_filename': 'css/syntaxhighlighter/styles/sh_compressed.r?.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    
    # other CSS groups goes here
}
COMPRESS_JS = {
    'syntaxhighlighter_js': {
        'source_filenames': (
                             'js/syntaxhighlighter/scripts/shCore.js', 
                             'js/syntaxhighlighter/scripts/shBrushBash.js', 
                             'js/syntaxhighlighter/scripts/shBrushJScript.js',
                             'js/syntaxhighlighter/scripts/shBrushPhp.js', 
                             'js/syntaxhighlighter/scripts/shBrushPlain.js',
                             'js/syntaxhighlighter/scripts/shBrushPython.js',
                             'js/syntaxhighlighter/scripts/shBrushSql.js',
                            ),
        'output_filename': 'js/syntaxhighlighter/scripts/sh_compressed.r?.js',
    },
    'jquery_js': {
        'source_filenames': (
                             'js/jquery-1.3.2.min.js',
                            ),
        'output_filename': 'js/jquery_compressed.r?.js',
    }
}

TINYMCE_JS_URL = MEDIA_URL + 'js/tiny_mce/tiny_mce.js'

TINYMCE_DEFAULT_CONFIG = {
    # General options
    'mode' : "textareas",
    'elements' : "elm2",
    'theme' : "advanced",
    'skin' : "o2k7",
    'plugins': "advimage,advlink,paste,media,\
                template,searchreplace,emotions,",
    'convert_fonts_to_spans' : 'true',
     # Theme options
    'font_size_style_values' : "12px,14px,18px,24px,36px",
    'theme_advanced_buttons1' : """paragraph, fontselect, fontsizeselect, 
                                 forecolor, bold, italic, underline, link, unlink,
                                 justifyleft, justifycenter, justifyright, 
                                 justifyfull, bullist, numlist, image, emotions, 
                                 code
                                 """,
    'theme_advanced_buttons2' : "",
    'theme_advanced_buttons3':'',
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location': "none",
    'theme_advanced_path': "false",
    'theme_advanced_font_sizes' : '12px=1, 14px=2, 18px=3, 24px=4, 36px=5',
    'width':'800',
    'height': '400',
    
    'dialog_type': "modal",
    'cleanup_on_startup': "true",
    'forced_root_block': "p",
    'remove_trailing_nbsp': "true",

    'advlink_styles': "internal (sehmaschine.net)=internal;\
                       external (link to an external site)=external",
    'advimage_update_dimensions_onchange': "true",
    'file_browser_callback': "CustomFileBrowser",
    'relative_urls': "false",
    'extended_valid_elements': "textarea[name|class|cols|rows]",  
    'remove_linebreaks' : "false", 
}


TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
