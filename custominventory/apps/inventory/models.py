from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Brand(models.Model):
    name = models.CharField(max_length=100)

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand,on_delete=models.CASCADE)
    
class CampaignDetail(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    purchase_price = models.FloatField(min=0)
    sale_price = models.FloatField(min=0)
    