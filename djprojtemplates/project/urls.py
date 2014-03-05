from django.conf.urls import patterns, url

from project.views import ProjectList, ProjectNew

urlpatterns = patterns('',
    url(r'^$', ProjectList.as_view(), name='list'),
    url(r'^project/new/$', ProjectNew.as_view(), name='new'),
)
