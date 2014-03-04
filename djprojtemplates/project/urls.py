from django.conf.urls import patterns, url

from project.views import ProjectList

urlpatterns = patterns('',
    url(r'^$', ProjectList.as_view(), name='list'),
)
