from django.contrib import admin
from basic.blog.models import *
from forms import PostAdminModelForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    form = PostAdminModelForm

    list_display  = ('title', 'publish', 'status')
    list_filter   = ('publish', 'categories', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        js = [ 
                ''.join([settings.MEDIA_URL,'/media/js/jquery-1.3.2.min.js']),
             ]

admin.site.register(Post, PostAdmin)
