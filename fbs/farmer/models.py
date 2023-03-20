from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Crops(models.Model):
    """
        MODEL TO STORE CROP NAMES
    """
    crop_name = models.CharField(max_length=100,null=False,blank=False)
    
    class Meta:
        db_table = "crops_name"


class FarmerCrops(models.Model):
    """

    """
    crop = models.ForeignKey(Crops,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quality = models.CharField(max_length=300,null=False,blank=False)
    quantity = models.IntegerField(default=0,null=False,blank=False)
    min_bid = models.IntegerField(default=0,null=False,blank=False)
    is_active = models.BooleanField(default=False)
    start_date = models.DateField(null=False,blank=False)
    end_date = models.DateField(null=False,blank=False)
    
    class Meta:
        db_table = "farmer_crops"


class Bidding(models.Model):
    """
    
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    farmer_crop = models.ForeignKey(FarmerCrops,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    comment = models.TextField(max_length=300)

    class Meta:
        db_table = "bidding"