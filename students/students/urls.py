from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'students.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('faculty.urls')),
    url(r'^group/', include('faculty.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
