from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
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


class GroupCreateView(CreateView):
    model = Group
    success_url = reverse_lazy('group-list')


class StudentCreateView(CreateView):
    model = Student

    def get_success_url(self):
        return reverse('group-details', args=(self.object.group.id,))


class StudentUpdateView(UpdateView):
    model = Student

    def get_success_url(self):
        return reverse('group-details', args=(self.object.group.id,))


class StudentDeleteView(DeleteView):
    model = Student

    def get_success_url(self):
        return reverse('group-details', args=(self.object.group.id,))
