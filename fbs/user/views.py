from django.shortcuts import render,redirect
from . import database_logic as logic
import logging
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from .models import AuthUserExtension


logger = logging.getLogger("error_logger")
# Create your views here.


def user_register(request):
    """
        ### register user
    """
    try:
        if request.method == 'POST':
            first_name=request.POST.get("firstName")
            last_name=request.POST.get("lastName")
            password=request.POST.get("password")
            mobile=request.POST.get("mobile")
            address=request.POST.get("address")
            state=request.POST.get("state")
            city=request.POST.get("city")
            gender=request.POST.get("gender")
            is_farmer=request.POST.get("is_farmer")
            print("Data>>>>>>",first_name,last_name,password,mobile,address,state,city,gender,is_farmer)
            data=logic.register_user(first_name,last_name,password,mobile,address,state,city,gender,is_farmer)
            if data:
                return redirect(user_login)
            else:
                return render(request, 'register.html')
        else:
            return render(request, 'register.html')
    except Exception as e:
        logger.error(f'{repr(e)} -->{request.user.username}')
    
def user_login(request):
    """
    Function is to use login for farmer & consumer both
    """
    try:
        if request.method == "POST":
            is_valid = validate_user(request)
            if is_valid["success"]:
                return redirect('home')
            else:
                messages.success(request, is_valid["message"])
                return render(request,'login.html')
        else:
            print("inside login get")
            return render(request,'login.html')
    except Exception as e:
        logger.error(f'{repr(e)} -->{request.user.username}')
        return redirect("error404")        
    
def validate_user(request):
    """
        METHOD IS BEING USED TO VALIDATE USER
    """
    try:
        contact_info = request.POST.get('contact_info')
        password = request.POST.get('password')

        user = AuthUserExtension.objects.filter(mobile=contact_info).exists()

        if user:
            user = auth.authenticate(username=contact_info,password=password)
            print("check password >> ",user)
            if not user:
                return {"success":False,"message":"Incorrect credentails"}
            else:
                auth.login(request,user)
                return {"success":True,"message":"login successfully"}
        else:
            return {"success":False,"message":"Incorrect credentails"}

    except Exception as e:
        logger.error(f'{repr(e)} -->{request.user.username}')
        return redirect("error404")