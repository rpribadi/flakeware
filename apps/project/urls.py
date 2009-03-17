from django.conf.urls.defaults import *
import views


urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$',
        view=views.project_detail,
        name='project_detail'),

    url(r'^tag/(?P<slug>[-\w]+)/$',
        view=views.tag_detail,
        name='project_tag_detail'),

    url (r'^search/$',
        view=views.search,
        name='project_search'),

    url(r'^page/(?P<page>\w)/$',
        view=views.project_list,
        name='project_index_paginated'),

    url(r'^$',
        view=views.project_list,
        name='project_index'),
)