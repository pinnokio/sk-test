from django.conf.urls import patterns, include, url

from django.contrib import admin
from faculty import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.GroupListView.as_view(), name='group-list'),

    url(r'^group/edit/(?P<pk>\d+)$', views.GroupDetailsView.as_view(),
                                     name='group-details'),
    url(r'^student/edit/(?P<pk>\d+)$', views.StudentUpdateView.as_view(),
                                       name='student-edit'),
    url(r'^student/delete/(?P<pk>\d+)$', views.StudentDeleteView.as_view(),
                                       name='student-delete'),
    url(r'^admin/', include(admin.site.urls)),
)
