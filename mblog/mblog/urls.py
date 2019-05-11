from django.conf.urls import include, url
from django.contrib import admin
from mainsite import views as v


urlpatterns = [
    # Examples:
    # url(r'^$', 'mblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', v.homepage_render),
    url(r'^post/(\w+)$', v.showpost),

]
