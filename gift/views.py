from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

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


class CreateListView(CreateView):

    model = List
    template_name = "edit_list.html"


class DeleteListView(DeleteView):

    model = List
    template_name = "list_confirm_delete.html"

    def get_success_url(self):
        return reverse("my_lists")

class DetailGiftView(DetailView,MembersOnlyView):

    model = Gift
    template_name = "detail_gift.html"