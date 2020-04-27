from django.contrib import admin
from .models import Category, Tag, Comment, Post
from pages.admin import ActionPublish
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


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


class PostAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    text = forms.CharField(required=False, label="Контент страницы", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(ActionPublish):
    inlines = [CommentsInline]
    filter_horizontal = ("tags",)
    list_display = ("title", "published", "id", 'category')
    list_editable = ("published", "category")
    list_filter = ("published", "template", "category")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    actions = ['unpublish', 'publish']
    save_on_top = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)

admin.site.site_title = "Да, это жестко"
admin.site.site_header = "Да, это жестко"



