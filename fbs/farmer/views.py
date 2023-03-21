from django.shortcuts import render,redirect,HttpResponse
from . import database_logic as logic
import logging
logger = logging.getLogger("error_logger")


# Create your views here.
def farmer_dashboard(request):
    """"
        
    """
    try:
        return render(request,'dashboard.html')
    except Exception as e:
        logger.error(f'{repr(e)} -->{request.user.username}')
        return redirect("error404")
    
def add_crop(request):
    """"

    """
    try:
        if request.method == "POST":
            crop_id=request.POST.get("cropType")
            quality=request.POST.get("cropQuality")
            quantity=request.POST.get("cropQuantity")
            min_bid=request.POST.get("minBid")
            start_date=request.POST.get("startDate")
            end_date=request.POST.get("endDate")
            data=logic.add_crop(crop_id,quality,quantity,min_bid,start_date,end_date,request.user.id)
            return redirect('farmer_dashboard')
        else:
            data=logic.get_add_crop(request)
            return render(request,'add_crop.html',data)
    except Exception as e:
        logger.error(f'{repr(e)} -->{request.user.username}')
    
