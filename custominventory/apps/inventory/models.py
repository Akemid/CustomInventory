from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Categoria"

class Brand(TimeStampedModel):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Marca"

class Campaign(TimeStampedModel):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta:
        verbose_name = "Campaña"
    
class Item(TimeStampedModel):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    description = models.CharField(max_length=300,null=True)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock = models.FloatField(default=0)
    image = models.ImageField(upload_to="items",null=True,blank=True)
    class Meta:
        verbose_name = "Producto"
    
class CampaignDetail(TimeStampedModel):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    purchase_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    
    class Meta:
        verbose_name = "Detalle de campaña"
        verbose_name_plural = "Detalles de campañas"

class Transaction(TimeStampedModel):
    
    TRANSACTION_TYPE = (
        ('I','Incoming'),
        ('O','Outgoing'),
    )
    
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    item_amount = models.FloatField(default=1)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE)    
    
    class Meta:
        verbose_name = "Transaccion"
        verbose_name_plural = "Transacciones"