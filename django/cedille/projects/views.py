from django.shortcuts import render
from django.views import generic
from projects.models import Project


class ProjectList(generic.ListView):
    model = Project
    template_name = 'view_projects.html'
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)

        context['myVariableOfContext'] = 0

        return context
