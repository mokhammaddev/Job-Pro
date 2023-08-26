from django.contrib import admin
from .models import Blog, TagBlog, SubContent, Comment


@admin.register(TagBlog)
class TagBlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'description', 'image', 'get_tags', 'created_date']

    def get_tags(self, obj):
        return ", ".join([tag.title for tag in obj.tags.all()])


@admin.register(SubContent)
class SubContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'title', 'image', 'description']


# COMMENT
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'name']



