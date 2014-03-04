# -*- coding: utf-8 -*-

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, Field

from project.models import Project


class ProjectForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Field('name', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('description', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('license', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('repository', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('site', css_class='form-control'),
            css_class='form-group'
        )
    )

    class Meta:
        model = Project
        exclude = ('created_at','slug',)
