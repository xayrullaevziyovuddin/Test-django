from django.contrib import admin
from .models import Post, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3  # Количество дополнительных полей для загрузки изображений

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    inlines = [ImageInline]

admin.site.register(Post, PostAdmin)
