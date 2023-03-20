from django.db import models

# Create your models here.
class Crops(models.Model):
    """
        MODEL TO STORE CROP NAMES
    """
    crop_name = models.CharField(max_length=100,null=False,blank=False)
    
    class Meta:
        db_table = "crops_name"