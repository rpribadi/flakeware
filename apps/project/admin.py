from django.contrib import admin
from models import Project, Log
from forms import ProjectForm, LogForm


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm

    list_display  = ('title','publish','status',)
    list_filter   = ('tags',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        js = [ 
                '/media/js/jquery-1.3.2.min.js',
             ]

class LogAdmin(admin.ModelAdmin):
    form = LogForm

    list_display  = ('title','created')
    list_filter   = ('project',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        js = [ 
                '/media/js/jquery-1.3.2.min.js',
             ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Log,LogAdmin)
