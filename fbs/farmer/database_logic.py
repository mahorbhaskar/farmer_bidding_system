from farmer.models import Crops,FarmerCrops
from django.contrib.auth.models import User


def add_crop(crop_id,quality,quantity,min_bid,start_date,end_date,user_id):
    '''
    Add crop to the database
    '''
    try:
        user=User.objects.filter(id=user_id)
        crop=Crops.objects.filter(id=crop_id)
        farmer_crop=FarmerCrops.objects.create(crop=crop[0],user=user[0],quality=quality,quantity=quantity,min_bid=min_bid,start_date=start_date,end_date=end_date)
        farmer_crop.save()
    except Exception as e:
        raise Exception(repr(e),"farmer/database_logic/add_crop/")


def get_add_crop(request):
    '''
    Get Add crop data from database
    '''
    try:
        crop=list(Crops.objects.all().values())
        return {'crop':crop}
    except Exception as e:
        raise Exception(repr(e),"farmer/database_logic/get_add_crop/")
