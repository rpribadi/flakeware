from django import forms
from django.db.models import get_model
from tinymce.widgets import TinyMCE

class ProjectForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE())
    tease = forms.CharField(widget=TinyMCE())
    
    class Meta:
        model = get_model('project', 'Project')

class LogForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE())
    
    class Meta:
        model = get_model('project', 'Log')
