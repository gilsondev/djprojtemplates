# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _

from project.models import Project


def publish(modeladmin, request, queryset):
    """Define project template to published"""
    for item in queryset:
        item.is_published = not item.is_published
        item.save()
publish.short_description = _(u"Publish/Unpublish project")


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['name', 'license', 'dj_version',
                    'repository_name', 'created_at', 'is_published']
    search_fields = ('name',)
    list_filter = ['created_at', 'dj_version']
    date_hierarchy = 'created_at'
    actions = [publish]

admin.site.register(Project, ProjectAdmin)
