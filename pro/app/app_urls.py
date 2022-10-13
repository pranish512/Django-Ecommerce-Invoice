from django.urls import path
from .app_views import *
from . import app_views as views

urlpatterns = [
    path('', views.home, name='home'),    
    # path('addproduct/', views.addproduct, name='addproduct'),    
    path('orderlist/', views.orderlist, name='orderlist'),    
    path('orderupdate/<int:id>/', views.orderupdates, name='orderupdate'),
    path('addProdUnit/', views.addProductUnit, name='addProdUnit'),
    # path('addproduct/', views.addProducts, name='addproduct'),
    path('addcustomer/', views.addCustomers, name='addcustomer'),
    path('cusdetailsremove/<int:id>', views.removecustomerdetails, name='cusdetailsremove'),
    # path('addunit/', views.addUnits, name='addunit'),
    path('deleteorderlist/<int:id>', views.remove, name='deleteorderlist'),
    path('productdetailsremove/<int:id>', views.removeproductdetail, name='productdetailsremove'),
    path('masterupdate/<int:id>/',views.masterUpdate, name='masterupdate')
    # path('orderdetails/', views.orderdetails, name='orderdetails')
]