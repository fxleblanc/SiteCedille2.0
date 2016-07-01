from django.shortcuts import render
from django.views import generic
from member.models import Member


class MemberList(generic.ListView):

    model = Member
    template_name = "view_member.html"
    context_object_name = "members"

    def get_context_data(self, **kwargs):
        context = super(MemberList, self).get_context_data(**kwargs)

        # Here you add some variable of context to display on template
        context['myVariableOfContext'] = 0

        return context
