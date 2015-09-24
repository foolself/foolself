from django.conf.urls import include, url
from django.contrib import admin
from blog.views import index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
]