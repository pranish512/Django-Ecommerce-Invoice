from django.urls import path
from .api_views import *

urlpatterns = [
    path('nestcusdetails/', NestCustomerDetailsGenerics.as_view()),
    path('nestunit/', NestUnitGenerics.as_view()),
    path('nestunit/<int:pk>/', NestEditUnitGenerics.as_view()),

    path('nestprod/', NestProductGenerics.as_view()),
    path('nestprod/<int:pk>/', NestEditProductGenerics.as_view()),

    path('nestorddetails/', NestOrderDetailsGenerics.as_view()),
    path('nestordlist/', NestOrderListGenerics.as_view()),

    path('postcusdetails/', PostCustomerDetailsGenerics.as_view()),
    path('editcusdetails/<int:pk>/', EditCustomerDetailsGenerics.as_view()),

    path('postunit/', PostUnitGenerics.as_view()),
    path('editunit/<int:pk>/', EditUnitGenerics.as_view()),

    path('postprod/', PostProductGenerics.as_view()),
    path('editprod/<int:pk>/', EditProductGenerics.as_view()),

    path('postorddetails/', PostOrderDetailsGenerics.as_view()),
    path('editorddetails/<int:pk>/', EditOrderDetailsGenerics.as_view()),

    path('postordlist/', PostOrderListGenerics.as_view()),
    path('editordlist/<int:pk>/', EditOrderListGenerics.as_view()),

    path('tablecusdetails/', TableCustomerDetailsGenerics.as_view()),
    path('tableorderlist/', TableOrderListGenerics.as_view()),
    path('nesttableorderlist/', TableOrderListNest.as_view()),
    path('nesttableorderlist/<int:pk>/', EditTableOrderListNest.as_view()),

    path('orderno/', DataCountGenerics.as_view()),

    path('nestlist/', DetailsInListGenerics.as_view()),
    path('nestlist/<int:pk>/', EditDetailsInListGenerics.as_view()),
    path('nestunitprod/', NestUnitProductsGenerics.as_view()),

    # NEW UPDATES URL IN NESTED FORM:::: 
    path('nestord2/', NestProductInOrderDetailsGenerics.as_view()), 
    path('nestlist2/', NestOrderDetailsInOrderGenerics.as_view()), 

    # path('multiplemodel/', MultipleModelViews.as_view()),
]
