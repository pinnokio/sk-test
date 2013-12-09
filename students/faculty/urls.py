from django.conf.urls import patterns, url

# from faculty import views
from faculty.views import GroupListView

urlpatterns = patterns('',
    url(r'^$', GroupListView.as_view(), name='group-list')
    # url(r'^$', views.group_list, name='group_list'),
)