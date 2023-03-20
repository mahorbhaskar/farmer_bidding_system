from user.models import AuthUserExtension
from django.contrib.auth.models import User


def register_user(first_name,last_name,password,mobile,address,state,city,gender,dob,is_farmer):
    '''
    REGISTER THE USER
    '''

    try:
        print("In database")
        user=User.objects.create(first_name=first_name,last_name=last_name,password=password,username=mobile)
        user.save()
        print("User>>",user)
        auth_user=AuthUserExtension.objects.create(mobile=mobile,is_farmer=is_farmer,dob=dob,address=address,city=city,state=state,user_id=user.id)
        auth_user.save()
        print("Auth user>>>>>",auth_user)
        return True
        
    except Exception as e:
        raise Exception(repr(e),"user/database_logic/save_user_info/")
