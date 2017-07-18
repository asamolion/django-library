from django.contrib import admin

from .models import Book, Subject
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'call_no', 'author', 'isbn',
                    'pub_date', 'edition', 'issue_date', 'return_date',)
    list_filter = ('call_no', 'pub_date', 'edition',
                   'issue_date', 'return_date',)


admin.site.register(Book, BookAdmin)
