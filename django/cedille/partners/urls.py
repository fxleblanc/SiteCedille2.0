from django.conf.urls import url
from partners.views import PartnerList

urlpatterns = [
    url(r'^', PartnerList.as_view(), name="partner_list"),
    url(r'^view/', PartnerList.as_view(), name="partner_list")
]
