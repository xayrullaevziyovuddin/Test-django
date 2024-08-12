from django.contrib import admin
from .models import Post, Image, Category
from taggit.models import Tag


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'get_categories', 'status')
    inlines = [ImageInline]
    fields = ('title', 'body', 'user', 'tags', 'category', 'status')

    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])

    get_categories.short_description = 'Categories'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)
