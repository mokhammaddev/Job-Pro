from django.contrib import admin
from .models import Jobs, CategoryJobs, TagJobs, SelectionList
#
#
# @admin.register(Jobs)
# class JobsAdmin(admin.ModelAdmin):
#     list_display = ['id', 'author', 'title', 'company', 'category', 'type', 'price', 'working_day',
#                     'tags', 'created_date']
#


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'company', 'get_type', 'get_tags', 'price', 'working_day', 'created_date']

    def get_tags(self, obj):
        return ", ".join([tag.title for tag in obj.tags.all()])

    def get_type(self, obj):
        return ", ".join([type1.title for type1 in obj.type.all()])


@admin.register(CategoryJobs)
class CategoryJobsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(TagJobs)
class TagJobsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(SelectionList)
class SelectionListAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'jobs']

