from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.base import View,TemplateView
from django.contrib.auth.models import User

class MembersOnlyView(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MembersOnlyView, self).dispatch(*args, **kwargs)

class HomeView(TemplateView):
    
    template_name = "home.html"