from django.conf.urls.defaults import *
import views


urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$',
        view=views.book_detail,
        name='book_detail'),

    url(r'^tag/(?P<slug>[-\w]+)/$',
        view=views.tag_detail,
        name='book_tag_detail'),

    url (r'^search/$',
        view=views.search,
        name='book_search'),

    url(r'^page/(?P<page>\w)/$',
        view=views.book_list,
        name='book_index_paginated'),

    url(r'^$',
        view=views.book_list,
        name='book_index'),
)