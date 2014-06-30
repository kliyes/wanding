from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wanding.views.home', name='home'),
    # url(r'^wanding/', include('wanding.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'product.views.home_page', name='index'),
    url(r'^about/$', 'product.views.about', name='about'),
    url(r'^idea/$', 'product.views.idea', name='idea'),
    url(r'^search/$', 'product.views.search', name='search'),
    url(r'^tag/$', 'product.views.serch_tag', name='tag'),

    (r'^product/', include('product.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        ),
    )
