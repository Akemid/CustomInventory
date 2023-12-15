from django.urls import path
from .views import InventoryHome,IndexView

app_name = 'inventory_app'


urlpatterns = [
    path('',InventoryHome.as_view(),name='inventory_home'),
    path('index/',IndexView.as_view(),name='index'),
]
