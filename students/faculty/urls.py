from django.conf.urls import patterns, url

from faculty import views

urlpatterns = patterns('',
    url(r'^$', views.GroupListView.as_view(), name='group-list'),
    url(r'^(?P<pk>\d+)$', views.GroupDetailsView.as_view(), name='group-details'),
)