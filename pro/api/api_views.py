from .models import *
from .serializer import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_multiple_model.views import FlatMultipleModelAPIView

# Create your views here.

# ======GENERICS FOR READONLY=======

class NestCustomerDetailsGenerics(generics.ListCreateAPIView):
    queryset = CustomerDetailsModel.objects.all()
    serializer_class = NestCutomerDetailsSerializer

#  ========= UNIT NEST and EDIT
class NestUnitGenerics(generics.ListCreateAPIView):
    queryset = UnitModel.objects.all()
    serializer_class = NestUnitSerialiazer

class NestEditUnitGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitModel.objects.all()
    serializer_class = NestUnitSerialiazer
# ==========

#  ========= PRODUCT NEST and EDIT
class NestProductGenerics(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = NestProductSerializer

class NestEditProductGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = NestProductSerializer

#  =========

class NestOrderDetailsGenerics(generics.ListCreateAPIView):
    queryset = OrderDetailsModel.objects.all()
    serializer_class = NestOrderDetaislSerializer

class NestOrderListGenerics(generics.ListCreateAPIView):
    queryset = OrderListModel.objects.all()
    serializer_class = NestOrderListSerializer

# ======GENERICS FOR POSTING DATA=======

class PostCustomerDetailsGenerics(generics.ListCreateAPIView):
    queryset = CustomerDetailsModel.objects.all()
    serializer_class = PostCutomerDetailsSerializer

class EditCustomerDetailsGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerDetailsModel.objects.all()
    serializer_class = UpdateCutomerDetailsSerializer

#==>
class PostUnitGenerics(generics.ListCreateAPIView):
    queryset = UnitModel.objects.all()
    serializer_class = PostUnitSerialiazer

class EditUnitGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitModel.objects.all()
    serializer_class = PostUnitSerialiazer

#==>
class PostProductGenerics(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = PostProductSerializer

class EditProductGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = UpdateProductSerializer

#==>
class PostOrderDetailsGenerics(generics.ListCreateAPIView):
    queryset = OrderDetailsModel.objects.all()
    serializer_class = PostOrderDetailsSerializer

    # def post(self, request, order_id):
    #     try:
    #         data = OrderListModel.objects.last()
    #         values = data.object_id+1
    #         return "OR%004d%" % values
    #     except:
    #         return "OR0001"
    #     # id =OrderListModel.objects.filter(order_id=)
    #     OrderDetailsModel.objects.filter(order_id='null').update(order_id=id)


class EditOrderDetailsGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetailsModel.objects.all()
    serializer_class = PostOrderDetailsSerializer

#==>
class PostOrderListGenerics(APIView):
    # queryset = OrderListModel.objects.all()
    # serializer_class = PostOrderListSerializer
    def get(self, request):
        ord_list = OrderListModel.objects.all()
        ord_list_serializer = PostOrderListSerializer(ord_list, many=True)
        return Response(ord_list_serializer.data)
    
    def post(self, request):
        ord_serializer = PostOrderListSerializer(data=request.data)
        if ord_serializer.is_valid():
            ord_serializer.save()
            return Response(ord_serializer.data, status=status.HTTP_200_OK)
        return Response(ord_serializer.errors, status=status.HTTP_400_BAD_REQUEST)         

class EditOrderListGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset =OrderListModel.objects.all()
    serializer_class = PostOrderListSerializer

# ========NEST DATE FOR ORDERLIST TABLE==========
class TableCustomerDetailsGenerics(generics.ListCreateAPIView):
    queryset = CustomerDetailsModel.objects.all()
    serializer_class = TableCutomerNest

class TableOrderListGenerics(generics.ListCreateAPIView):
    queryset = OrderListModel.objects.all()
    serializer_class = TableOrderList

class TableOrderListNest(generics.ListCreateAPIView):
    queryset = OrderListModel.objects.all()
    serializer_class = TableOrderListSerializer

class EditTableOrderListNest(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderListModel.objects.all()
    serializer_class = TableOrderListSerializer

class DataCountGenerics(generics.ListAPIView):
    queryset = OrderListModel.objects.all()
    serializer_class = DataCount

class DetailsInListGenerics(generics.ListAPIView):
    queryset = OrderListModel.objects.all()
    serializer_class = NestDetailsInList

class EditDetailsInListGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderListModel.objects.all()
    serializer_class = NestDetailsInList

class NestUnitProductsGenerics(generics.ListCreateAPIView):
    queryset = UnitModel.objects.all()
    serializer_class = UnitProdNest

class NestProductInOrderDetailsGenerics(generics.ListCreateAPIView):
    queryset = OrderDetailsModel.objects.all()
    serializer_class = NestProductInOrderDetailsSerializer

class NestOrderDetailsInOrderGenerics(generics.ListCreateAPIView):
    queryset = OrderListModel.objects.all()
    serializer_class = NestOrderDetailsInOrderSerizlizer

# DRF MULTIPLE MODELS::::
# class MultipleModelViews(FlatMultipleModelAPIView):
#     pagination_class = None
#     add_model_type = False
#     querylist = [
#         {'queryset': OrderDetailsModel.objects.filter(order_id_id=OrderListModel.order_id), 'serializer_class': NestProductInOrderDetailsSerializer},
#         {'queryset': OrderListModel.objects.all(), 'serializer_class': NestOrderDetailsInOrderSerizlizer},
#     ]