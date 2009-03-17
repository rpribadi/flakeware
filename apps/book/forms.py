from django import forms
from django.db.models import get_model
from tinymce.widgets import TinyMCE

class BookForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE())
    tease = forms.CharField(widget=TinyMCE())
    
    class Meta:
        model = get_model('book', 'Book')
