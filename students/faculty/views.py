from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from faculty.models import Group, Student

class GroupListView(ListView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        return context

class GroupDetailsView(DetailView):
    model = Group
    template_name = "faculty/group_details.html"
    
    def get_context_data(self, **kwargs):
        context = super(GroupDetailsView, self).get_context_data(**kwargs)
        return context