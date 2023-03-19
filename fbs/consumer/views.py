from django.shortcuts import render,redirect
import logging


logger = logging.getLogger("error_logger")
# Create your views here.


def home(request):
    """
        ### home page
    """
    try:
        return render(request, 'home.html')
        
    except Exception as e:
        logger.error(f'{repr(e)} -->{request.user.username}')
        return redirect("error404")