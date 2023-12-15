from django.contrib import admin
from .models import Item,Brand, Campaign, CampaignDetail,Category,Transaction
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    '''Admin View for Item'''

    list_display = [field.name for field in Item._meta.fields]
    #list_filter = ('',)
    search_fields = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    '''Admin View for Brand'''

    list_display = [field.name for field in Brand._meta.fields]
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = [field.name for field in Category._meta.fields]
    search_fields = ('name',)

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    '''Admin View for Campaign'''

    list_display = [field.name for field in Campaign._meta.fields]
    search_fields = ('name','start_date')

@admin.register(CampaignDetail)
class CampaignDetailAdmin(admin.ModelAdmin):
    '''Admin View for CampaignDetail'''

    list_display = [field.name for field in CampaignDetail._meta.fields]
    search_fields = ('campaign__name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    '''Admin View for Transaction'''

    list_display = [field.name for field in Transaction._meta.fields]
    list_filter = ('transaction_type',)
    search_fields = ('campaign__name',)