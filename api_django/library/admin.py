from django.contrib import admin
from library.models import BookAuthor, Book


class AuthorsInline(admin.TabularInline):
    model = Book


@admin.register(BookAuthor)
class AuthorsBookAdmin(admin.ModelAdmin):
    list_filter = ['date_of_birth', 'date_of_death', 'created_at']
    search_fields = ['first_name', 'last_name']
    inlines = [AuthorsInline]


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_filter = ['book_status', 'created_at']
    search_fields = ['name']

    actions = ['mark_as_published', 'mark_as_deleted']

    def mark_as_published(self, request, queryset):
        queryset.update(book_status=Book.PUBLISHED)

    def mark_as_deleted(self, request, queryset):
        queryset.update(book_status=Book.DELETED)

    mark_as_published.short_description = 'Статус опубликовано'
    mark_as_deleted.short_description = 'Снято из пула книг'
