from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from tagging.fields import TagField
from managers import PublicManager

import tagging


class Project(models.Model):
    """Project model."""
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
    title           = models.CharField(_('title'), max_length=200)
    slug            = models.SlugField(_('slug'), unique_for_date='publish')
    author          = models.ForeignKey(User,related_name="working_for")
    image           = models.FileField(upload_to="uploads/projects")
    body            = models.TextField(_('body'))
    tease           = models.TextField(_('tease'), blank=True)
    status          = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    allow_comments  = models.BooleanField(_('allow comments'), default=True)
    publish         = models.DateTimeField(_('publish'))
    created         = models.DateTimeField(_('created'), auto_now_add=True)
    modified        = models.DateTimeField(_('modified'), auto_now=True)
    tags            = TagField()
    objects         = PublicManager()

    class Meta:
        verbose_name = _('Project Journal')
        verbose_name_plural = _('Project Journals')
        ordering  = ('-publish',)
        get_latest_by = 'publish'

    class Admin:
        list_display  = ('title', 'publish', 'status')
        list_filter   = ('tags',)
        search_fields = ('title', 'body')

    def __unicode__(self):
        return u'%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('project_detail', None, {
            'slug': self.slug
        })
    
    def get_previous_post(self):
        return self.get_previous_by_publish(status__gte=2)
    
    def get_next_post(self):
        return self.get_next_by_publish(status__gte=2)
    
class Log(models.Model):
    project         = models.ForeignKey(Project,related_name="log_project_for")
    title           = models.CharField(_('title'), max_length=200)
    slug            = models.SlugField(_('slug'), unique_for_date='created')
    body            = models.TextField(_('body'))
    created         = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta:
        verbose_name = _('Logs')
        verbose_name_plural = _('Logs')
        ordering  = ('-created',)
        get_latest_by = 'created'

    class Admin:
        list_display  = ('title', 'created', 'project')
        list_filter   = ('project',)
        search_fields = ('title', 'body')

    def __unicode__(self):
        return u'%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('project_detail_log', None, {
            'slug': self.slug
        })