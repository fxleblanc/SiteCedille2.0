from django.conf.urls import url
from projects.views import ProjectList

urlpatterns = [
    url(r'^', ProjectList.as_view(), name="project_list"),
    url(r'^view/', ProjectList.as_view(), name="project_list")
]
