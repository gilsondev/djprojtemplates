# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from project.models import Project
from project.forms import ProjectForm


class ProjectList(ListView):
    model = Project

    def get_queryset(self):
        """List projects published"""
        return Project.published.all()


class ProjectNew(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project:list')
