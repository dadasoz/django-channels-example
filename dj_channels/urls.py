from django.conf.urls import include, url
from django.contrib import admin

from mychannel import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^admin/', include(admin.site.urls)),
]
