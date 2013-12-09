from django.conf.urls import patterns, include, url

from django.contrib import admin
from faculty import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'students.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', include('faculty.urls')),
    url(r'^$', views.GroupListView.as_view(), name='group-list'),
    # url(r'^group/', include('faculty.urls')),
    # url(r'^student/', include('faculty.urls')),
    url(r'^group/edit/(?P<pk>\d+)$', views.GroupDetailsView.as_view(),
                                     name='group-details'),
    url(r'^student/edit/(?P<pk>\d+)$', views.StudentUpdateView.as_view(),
                                       name='student-edit'),
    url(r'^admin/', include(admin.site.urls)),
)
