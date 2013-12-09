from django.views.generic.list import ListView

from faculty.models import Group

class GroupListView(ListView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        return context

# from django.shortcuts import render
# from django.http import HttpResponse

# def group_list(request):
#     return HttpResponse("Group list")