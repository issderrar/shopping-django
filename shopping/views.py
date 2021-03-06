from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Index(TemplateView):
    """
    Index view
    """

    template_name = "shopping/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'test': 42})
