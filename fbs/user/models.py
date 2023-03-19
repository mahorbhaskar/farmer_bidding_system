from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AuthUserExtension(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=100,null=False,blank=False)
    is_farmer = models.BooleanField(default=0)
    dob = models.DateField(blank=True,null=True)
    dp = models.ImageField(upload_to='user/',null=True,blank=True)
    address = models.CharField(max_length=100,null=False,blank=False)
    city = models.CharField(max_length=100,null=False,blank=False)
    state = models.CharField(max_length=100,null=False,blank=False)

    class Meta:
        db_table = 'auth_user_extension'