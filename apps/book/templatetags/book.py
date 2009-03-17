from django import template
from django.conf import settings
from django.db import models

import re

Book = models.get_model('book', 'Book')

register = template.Library()


class LatestBooks(template.Node):
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name

    def render(self, context):
        books = Book.objects.published()[:int(self.limit)]
        if books and (int(self.limit) == 1):
            context[self.var_name] = books[0]
        else:
            context[self.var_name] = books
        return ''

@register.tag
def get_latest_book(parser, token):
    """
    Gets any number of latest posts and stores them in a varable.

    Syntax::

        {% get_latest_book [limit] as [var_name] %}

    Example usage::

        {% get_latest_book 10 as latest_book_list %}
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    format_string, var_name = m.groups()
    return LatestBooks(format_string, var_name)
