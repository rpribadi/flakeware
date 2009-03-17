from django import forms
from django.db.models import get_model
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())
    
    class Meta:
        model = FlatPage

