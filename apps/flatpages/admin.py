from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from forms import FlatPageForm


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageForm
    class Media:
        js = [ 
                '/media/js/jquery-1.3.2.min.js',
             ]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

