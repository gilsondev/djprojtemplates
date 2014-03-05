# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _

from project.models import Project


def make_published(modeladmin, request, queryset):
    """Define project template to published"""
    queryset.update(published=True)
make_published.short_description = _(u"Mark selected project as published")


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['name', 'license', 'dj_version',
                    'repository_name', 'created_at', 'published']
    search_fields = ('name',)
    list_filter = ['created_at', 'dj_version']
    date_hierarchy = 'created_at'
    actions = [make_published]

admin.site.register(Project, ProjectAdmin)
