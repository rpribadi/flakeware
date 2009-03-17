from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^flakeware/', include('flakeware.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$','basic.blog.views.post_list'),
    (r'^blog/',include('basic.blog.urls')),    
    (r'^tinymce/', include('tinymce.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^project/', include('project.urls')),
    (r'^book/', include('book.urls')),

    (r'^admin/filebrowser/', include('filebrowser.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )