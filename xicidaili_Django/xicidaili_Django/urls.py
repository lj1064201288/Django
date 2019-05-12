from django.conf.urls import include, url
from django.contrib import admin
from xici import urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'xicidaili_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(urls)),
]
