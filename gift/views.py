from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django.core.urlresolvers import reverse

from giftslist.views import MembersOnlyView

from gift.models import List, Gift


class ListOfListsView(ListView,MembersOnlyView):

    model = List
    context_object_name = "list_of_lists"
    template_name = "list_of_lists.html"


class MyListsView(ListOfListsView,MembersOnlyView):

    pass


class DetailListView(DetailView,MembersOnlyView):

    model = List
    template_name = "detail_list.html"


class EditListView(UpdateView):

    model = List
    template_name = "edit_list.html"
    
    def get_success_url(self):
        success_url = reverse("detail_list", kwargs={'pk': self.get_object().id})
        return success_url


class DetailGiftView(DetailView,MembersOnlyView):

    model = Gift
    template_name = "detail_gift.html"