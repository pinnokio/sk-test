from django.conf.urls import patterns, include, url

from django.contrib import admin
from faculty import views
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login'), 
                           # {'template_name': 'registration/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^$', login_required(views.GroupListView.as_view()), 
               name='group-list'),
    url(r'^group/edit/(?P<pk>\d+)$', views.GroupDetailsView.as_view(),
                                     name='group-details'),
    url(r'^group/create', views.GroupCreateView.as_view(),
                                        name='group-create'),
    url(r'^student/create', views.StudentCreateView.as_view(),
                                        name='student-create'),
    url(r'^student/edit/(?P<pk>\d+)$', views.StudentUpdateView.as_view(),
                                       name='student-edit'),
    url(r'^student/delete/(?P<pk>\d+)$', views.StudentDeleteView.as_view(),
                                       name='student-delete'),
    url(r'^admin/', include(admin.site.urls)),
)
