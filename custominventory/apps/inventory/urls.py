from django.urls import path
from .views import InventoryHome

app_name = 'inventory_app'


urlpatterns = [
    path('',InventoryHome.as_view(),name='inventory_home'),
]
