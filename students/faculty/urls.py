from django.conf.urls import patterns, url

from faculty import views

urlpatterns = patterns('',
    # url(r'^$', views.GroupListView.as_view(), name='group-list'),
    # url(r'^edit/(?P<pk>\d+)$', views.GroupDetailsView.as_view(), name='group-details'),
    # url(r'^edit/(?P<pk>\d+)$', views.StudentUpdateView.as_view(), name='student-edit'),
)