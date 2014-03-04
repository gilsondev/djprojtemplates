# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Project(models.Model):
    name = models.CharField(_(u"Project name"), max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(_(u"Description"), max_length=150)
    license = models.CharField(_(u"License"), max_length=20)
    repository = models.URLField(_(u"Repository URL"))
    site = models.URLField(_(u"Site URL"))
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.do_unique_slug()
        super(Project, self).save(*args, **kwargs)

    class Meta:
        db_table = "project"
        ordering = ['created_at']

    def do_unique_slug(self):
        """
        Ensure that the slug is always unique for this post
        """
        if not self.id:
            # make sure we have a slug first
            if not len(self.slug.strip()):
                self.slug = slugify(self.name)

            self.slug = self.get_unique_slug(self.slug)

    def get_unique_slug(self, slug):
        """
        Iterate until a unique slug is found
        """
        orig_slug = slug
        counter = 1

        while True:
            projects = Project.objects.filter(slug=slug)
            if not projects.exists():
                return slug

            slug = '%s-%s' % (orig_slug, counter)
            counter += 1
