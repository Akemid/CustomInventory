from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

class Brand(TimeStampedModel):
    name = models.CharField(max_length=100)

class Campaign(TimeStampedModel):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
class Item(TimeStampedModel):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock = models.FloatField(default=0)
    
class CampaignDetail(TimeStampedModel):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    purchase_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)

class Transaction(TimeStampedModel):
    
    TRANSACTION_TYPE = (
        ('I','Incoming'),
        ('O','Outgoing'),
    )
    
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    item_amount = models.FloatField(default=1)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE)    