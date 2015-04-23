from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
urlpatterns = [
    # Examples:
    # url(r'^$', 'Proyecto2_201020397.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, } ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.inicio.urls')),
	url(r'^', include('apps.dropbox.urls')),
	url(r'^', include('apps.WebService.urls')),
]
