# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from gift.models import List, Gift


class ListOfListsView(ListView):
    
    model = List
    context_object_name = "list_of_lists"
    template_name = "list_of_lists.html"
    

class MyListsView(ListOfListsView):
    
    pass

class DetailListView(DetailView):
    
    model = List
    template_name = "detail_list.html"
    
    
class DetailGiftView(DetailView):
    
    model = Gift
    template_name = "detail_gift.html"