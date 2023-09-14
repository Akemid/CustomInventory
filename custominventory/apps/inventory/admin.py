from django.contrib import admin
from .models import Item
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    '''Admin View for Item'''

    list_display = [field.name for field in Item._meta.fields]
    #list_filter = ('',)
    search_fields = ('name',)