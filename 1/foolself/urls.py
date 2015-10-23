from django.conf.urls import include, url
from django.contrib import admin
from blog.views import index, download, uploads
from django.conf.urls import patterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    url(r'^download/(?P<f>.*)$', download, name = "download"),
   url(r'^uploads', uploads, name ="uploads")
]
'''
urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    )
'''