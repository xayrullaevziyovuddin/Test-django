from django.contrib import admin
from .models import Post, Image, Tag, Author, Category


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'get_categories')
    inlines = [ImageInline]

    fields = ('title', 'body', 'author', 'tags', 'category')

    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])

    get_categories.short_description = 'Categories'

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Регистрация моделей в админке
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
