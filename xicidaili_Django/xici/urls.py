from django.conf.urls import include, url
from django.contrib import admin
from .views import daili
from .views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'xicidaili_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^daili/', daili),
    url(r'^index/', index),
]
