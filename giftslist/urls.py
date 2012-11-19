from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from gift.views import ListOfListsView, MyListsView, DetailListView, DetailGiftView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'giftslist.views.home', name='home'),
    # url(r'^giftslist/', include('giftslist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^lists/$', ListOfListsView.as_view(), name="list_of_lists"),
    url(r'^lists/my/$', MyListsView.as_view(), name="my_lists"),
    url(r'^lists/(?P<pk>\d+)$', DetailListView.as_view(), name="detail_list"),
    
    url(r'^gifts/(?P<pk>\d+)$', DetailGiftView.as_view(), name="detail_gift"),
)
