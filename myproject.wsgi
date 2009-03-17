import os
import sys
from os.path import abspath, dirname, join
from django.core.handlers.wsgi import WSGIHandler


sys.path = ['/home/rpribadi/webapps/flakeware_app', '/home/rpribadi/webapps/flakeware_app/lib/python2.5'] + sys.path

workspace = abspath(join(dirname(__file__)))
sys.path.append(join(workspace, 'flakeware'))
sys.path.insert(0, os.path.abspath(os.path.join(workspace, 'flakeware', 'apps')))



from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'flakeware.settings'
application = WSGIHandler()
