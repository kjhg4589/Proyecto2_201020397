from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'apps.inicio.views.index'),
]