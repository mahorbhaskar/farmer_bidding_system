from django.shortcuts import render,redirect
import logging
from django.contrib.auth.decorators import login_required
from .models import AuthUserExtension


logger = logging.getLogger("error_logger")
# Create your views here.


def user_register(request):
    """
        ### register user
    """
    try:
        return render(request, 'register.html')
        
    except Exception as e:
        logger.error(f'{repr(e)} -->{request.user.username}')
        return redirect("error404")
    
def user_login(request):
    """
    Function is to use login for farmer & consumer both
    """
    try:
        if(request.method == "POST"):
            contact_info = request.POST.get('contact_info')
            password = request.POST.get('password')
            print("contact >> ",contact_info)
            print("password >> ",password)
            user = AuthUserExtension.objects.filter(mobile=contact_info).exists()
            print("user >> ",user)
            if user:
                print("user exists")
            else:
                print("user no exists")
            print("inside login post")
            return render(request,'login.html')
        else:
            print("inside login get")
            return render(request,'login.html')
    except Exception as e:
        logger.error(f'{repr(e)} -->{request.user.username}')
        return redirect("error404")        