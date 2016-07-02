from django.shortcuts import render
from django.views import generic
from partners.models import Partner


class PartnerList(generic.ListView):
    model = Partner
    template_name = 'view_partners.html'
    context_object_name = "partners"

    def get_context_data(self, **kwargs):
        context = super(PartnerList, self).get_context_data(**kwargs)

        context['myVariableOfContext'] = 0

        return context
