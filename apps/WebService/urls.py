from django.conf.urls import url


urlpatterns = [
    url(r'^wService/dropbox/usuarios/$', 'apps.WebService.views.usuarios_view'),
]