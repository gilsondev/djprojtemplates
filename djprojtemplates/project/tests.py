# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from project.models import Project
from project.forms import ProjectForm


class ProjectListTest(TestCase):

    """Testcase to test project list"""

    def setUp(self):
        self.resp = self.client.get(reverse('project:list'))

    def test_get(self):
        """GET / must return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Should render template project/project_list.html"""
        self.assertTemplateUsed(self.resp, 'project/project_list.html')


class ProjectFormTest(TestCase):
    def setUp(self):
        self.form = ProjectForm()

    def test_fields(self):
        """Should have these fields"""
        fields = ['name', 'description', 'license',
                  'dj_version', 'repository', 'site', 'captcha']
        self.assertItemsEqual(fields, self.form.fields)


class ProjectModelTest(TestCase):

    """Testcase to test Project model"""

    def setUp(self):
        self.project = Project.objects.create(
            name="Project Template",
            description="Description Test",
            license="GPL",
            dj_version="django_15",
            repository="http://github.com/user/project",
            site="http://projectapp.com",
            is_published=False
        )

    def test_create(self):
        """Should create correctly"""
        self.assertEqual(self.project.pk, 1)

    def test_create_slug(self):
        """Should generate slug correctly"""
        self.assertEqual(self.project.slug, "project-template")
