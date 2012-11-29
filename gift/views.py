from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from django.core.urlresolvers import reverse

from giftslist.views import MembersOnlyView

from gift.models import List, Gift, GiftLink


class ListOfListsView(ListView,MembersOnlyView):

    model = List
    context_object_name = "list_of_lists"
    template_name = "list_of_lists.html"


class MyListsView(ListOfListsView,MembersOnlyView):

    pass


class DetailListView(DetailView,MembersOnlyView):

    model = List
    template_name = "detail_list.html"


class EditListView(UpdateView, MembersOnlyView):

    model = List
    template_name = "edit_list.html"


class CreateListView(CreateView, MembersOnlyView):

    model = List
    template_name = "edit_list.html"


class DeleteListView(DeleteView, MembersOnlyView):

    model = List
    template_name = "list_confirm_delete.html"

    def get_success_url(self):
        return reverse("my_lists")

class AddGiftView(CreateView,MembersOnlyView):

    model = Gift
    template_name = "edit_gift.html"





class DetailGiftView(DetailView,MembersOnlyView):

    model = Gift
    template_name = "detail_gift.html"


class EditGiftView(UpdateView, MembersOnlyView):

    model = Gift
    template_name = "edit_gift.html"


class DeleteGiftView(DeleteView, MembersOnlyView):

    model = Gift
    template_name = "gift_confirm_delete.html"


class AddGiftLinkView(CreateView, MembersOnlyView):

    model = GiftLink
    template_name = "edit_link.html"
    gift = None

    def get_context_data(self,**kwargs):
        context = super(AddGiftLinkView,self).get_context_data(**kwargs)
        self.gift = Gift.objects.get(pk=self.kwargs['pk'])
        context['predefined'] = {'gift': self.gift}
        return context






class EditLinkView(UpdateView, MembersOnlyView):

    model = GiftLink
    template_name = "edit_link.html"


class DeleteLinkView(DeleteView, MembersOnlyView):

    model = GiftLink
    template_name = "link_confirm_delete.html"
    
    def get_success_url(self):
        return self.object.gift.get_absolute_url()