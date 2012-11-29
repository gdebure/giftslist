from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout_then_login,password_change,password_change_done
from giftslist.views import HomeView
from gift.views import ListOfListsView, MyListsView, DetailListView
from gift.views import EditListView, CreateListView, DeleteListView

from gift.views import AddGiftView

from gift.views import DetailGiftView
from gift.views import EditGiftView, DeleteGiftView, AddGiftLinkView

from gift.views import EditLinkView, DeleteLinkView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'giftslist.views.home', name='home'),
    # url(r'^giftslist/', include('giftslist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin site:
    url(r'^admin/', include(admin.site.urls)),

    # Authentication stuff
    url(r'^login/', login, name="login"),
    url(r'^logout/$', logout_then_login, {'login_url' : '/login'}, name="logout"),
    url(r'^change_password/$', password_change, {'post_change_redirect' : '/change_password/done/'},name="password_change"),
    url(r'^change_password/done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}, name="password_change_done"),

    # Home
    url(r'^$', HomeView.as_view(), name="home"),

    # Lists URL
    url(r'^lists/$', ListOfListsView.as_view(), name="list_of_lists"),
    url(r'^lists/my/$', MyListsView.as_view(), name="my_lists"),
    url(r'^lists/create/$', CreateListView.as_view(), name="create_list"),
    url(r'^lists/(?P<pk>\d+)/$', DetailListView.as_view(), name="detail_list"),
    url(r'^lists/(?P<pk>\d+)/edit/$', EditListView.as_view(), name="edit_list"),
    url(r'^lists/(?P<pk>\d+)/delete/$', DeleteListView.as_view(), name="delete_list"),
    url(r'^lists/(?P<pk>\d+)/addgift/$', AddGiftView.as_view(), name="add_gift"),

    # Gifts URL
    url(r'^gifts/(?P<pk>\d+)$', DetailGiftView.as_view(), name="detail_gift"),
    url(r'^gifts/(?P<pk>\d+)/edit/$', EditGiftView.as_view(), name="edit_gift"),
    url(r'^gifts/(?P<pk>\d+)/delete/$', DeleteGiftView.as_view(), name="delete_gift"),
    url(r'^gifts/(?P<pk>\d+)/addlink/$', AddGiftLinkView.as_view(), name="add_gift_link"),

    # Links URL
    url(r'^giftlinks/(?P<pk>\d+)/edit/$', EditLinkView.as_view(), name="edit_link"),
    url(r'^giftlinks/(?P<pk>\d+)/delete/$', DeleteLinkView.as_view(), name="delete_link"),
)
