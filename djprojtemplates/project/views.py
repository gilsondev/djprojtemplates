# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from project.models import Project
from project.forms import ProjectForm


class ProjectList(ListView):
    model = Project


class ProjectNew(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project:list')

