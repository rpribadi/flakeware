from django.contrib import admin
from models import Book
from forms import BookForm


class BookAdmin(admin.ModelAdmin):
    form = BookForm

    list_display  = ('title','publish','status',)
    list_filter   = ('tags',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        js = [ 
                '/media/js/jquery-1.3.2.min.js',
             ]

admin.site.register(Book, BookAdmin)
