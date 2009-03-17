from django import template
from django.conf import settings
from django.db import models

import re

Project = models.get_model('project', 'Project')

register = template.Library()


class LatestProjects(template.Node):
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name

    def render(self, context):
        projects = Project.objects.published()[:int(self.limit)]
        if projects and (int(self.limit) == 1):
            context[self.var_name] = projects[0]
        else:
            context[self.var_name] = projects
        return ''

@register.tag
def get_latest_project(parser, token):
    """
    Gets any number of latest posts and stores them in a varable.

    Syntax::

        {% get_latest_project [limit] as [var_name] %}

    Example usage::

        {% get_latest_project 10 as latest_project_list %}
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    return LatestProjects(format_string, var_name)
