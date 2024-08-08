from django.contrib import admin
from .models import Post, Image, Tag, Author

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    inlines = [ImageInline]

    fields = ('title', 'body', 'author', 'tags')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Регистрация моделей в админке
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
