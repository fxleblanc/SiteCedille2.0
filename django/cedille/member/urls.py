from django.conf.urls import url
from member.views import MemberList

urlpatterns = [
    url(r'^view/', MemberList.as_view(), name='member_list'),
    url(r'^', MemberList.as_view(), name="member_list")
]
