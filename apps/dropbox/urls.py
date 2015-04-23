from django.conf.urls import url


urlpatterns = [
    # Examples:
    # url(r'^$', 'Proyecto2_201020397.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dropbox/$', 'apps.dropbox.views.inicio_view'),
    url(r'^dropbox/login/$', 'apps.dropbox.views.login_view'),
	url(r'^dropbox/register/$', 'apps.dropbox.views.register_view'),
	url(r'^dropbox/dropbox/$', 'apps.dropbox.views.dropbox_view'),
	url(r'^dropbox/crear/$', 'apps.dropbox.views.crear_view'),
	url(r'^dropbox/agregar/$', 'apps.dropbox.views.agregar_view'),
]