from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
import xadrpy.router.urls
from django.conf import settings

admin.autodiscover()
xadrpy.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),    
    url(r'^admin/rosetta/', include('rosetta.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^test/$', 'pacsee.views.test'),    
    
)
urlpatterns+=xadrpy.router.urls.urlpatterns

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )