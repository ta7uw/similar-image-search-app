from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Item
# Create your views here.


class TopPage(TemplateView):
    template_name = "index.html"


class SearchResultView(ListView):
    template_name = "result.html"
    model = Item

