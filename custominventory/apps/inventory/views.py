from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class InventoryHome(TemplateView):
    template_name = "inventory/inventory_home.html"