from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_dev_manage.views.home', name='home'),
    # url(r'^django_dev_manage/', include('django_dev_manage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url( r'^index/', direct_to_template, {
        'template':'index.html'
        }),
    #url( r'^login/', direct_to_template, {
    #    'template':'login.html'
    #    }),
    #url( r'^sub_login/', 'django_dev_manage.views.user_login' ),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page':'/index/' }),
    url(r'^person/$', 'device.views.per_info' ),
    url( r'^chg_usr/$', 'django_dev_manage.views.change_user' ),
)
