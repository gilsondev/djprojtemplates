# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Project
from .forms import ProjectForm


class ProjectList(ListView):
    model = Project
