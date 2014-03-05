# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

from captcha.fields import CaptchaField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Field, HTML

from project.models import Project


class ProjectForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

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
            Field('dj_version', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('repository', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('site', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('captcha', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Submit('register', _(u"Register Project Template"),
                   css_name='btn btn-lg btn-success'),
            HTML('<a href="{% url "project:list" %}" class="btn '
                 'btn-default">Back</a>'),
            css_class='text-center'
        )
    )

    class Meta:
        model = Project
        exclude = ('created_at', 'slug', 'published',)
