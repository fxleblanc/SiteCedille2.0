from django.conf.urls import url, include
from django.contrib import admin
from page.views import home

urlpatterns = [
    url(
        r'^home$',
        home,
        name='home'
       ),
]
