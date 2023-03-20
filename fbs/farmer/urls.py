from django.urls import path
from . import views

urlpatterns = [

    path('',views.farmer_dashboard,name='farmer_dashboard'),
    path('add_crop/',views.add_crop,name='add_crop'),
]