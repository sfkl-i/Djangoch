from django.contrib import admin
from .models import Category, Tag, Comment, Post
from pages.admin import ActionPublish


class CategoryAdmin(ActionPublish):
    """Категории блога"""
    list_display = ("id", "name", "parent", "slug", "paginated", "sort", "published")
    list_display_links = ("name",)
    list_filter = ("parent", )
    # exclude = ("sort", )
    # fieldsets
    # inlines =
    actions = ['unpublish', 'publish']


class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(ActionPublish):
    """Посты блога"""
    inlines = [CommentsInline]
    filter_horizontal = ("tags",)
    fieldsets = (
        ('Контент', {
            'fields': ('author', 'title', 'subtitle', 'slug'),
        }),
        ('Контент 2', {
            'fields': ('mini_text', 'text', 'image'),
        }),
        ('Даты', {
            'fields': ('edit_date', 'published_date'),
        }),
        ('Завязки', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('tags', 'category'),
        }),
        ('Настройки', {
            'classes': ('collapse',),
            'fields': ('template', 'published', 'status', 'sort', 'viewed'),
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)

admin.site.site_title = "Да, это жестко"
admin.site.site_header = "Да, это жестко"



