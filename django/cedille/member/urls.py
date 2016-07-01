from django.conf.urls import url
from member.views import MemberList
from django.conf.urls.static import static


urlpatterns = [
    url(r'^view/', MemberList.as_view(), name='member_list')
]
