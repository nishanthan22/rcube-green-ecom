from django.contrib import admin
from .models import NewsArticle, Tag

class NewsArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'date_posted', 'updated_at', 'views')
    list_filter = ('category', 'author')
    search_fields = ('title', 'content', 'tags__name')

admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(Tag)
