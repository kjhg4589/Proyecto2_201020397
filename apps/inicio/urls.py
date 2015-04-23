from django.conf.urls import patterns,include, url
from .views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'Proyecto2_201020397.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'apps.inicio.views.index'),
]