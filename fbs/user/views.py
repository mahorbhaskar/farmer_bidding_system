from django.shortcuts import render,redirect
import logging


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