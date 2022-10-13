from asyncio.windows_events import NULL
from itertools import product
from operator import mod
from pyexpat import model
from rest_framework import serializers
from .models import *
from django.db.models import Count, F, Value

# ======READONLY SERIALIZER DATA=======

class NestUnitSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = UnitModel
        fields =  ['unit_id', 'product_id', 'unit'] 

class NestProductSerializer(serializers.ModelSerializer):
    units = NestUnitSerialiazer(read_only=True, many=True)
    class Meta:
        model = ProductModel
        fields = ['product_id', 'product_name', 'units', 'price']

class NestOrderListSerializer(serializers.ModelSerializer):   
    class Meta:
        model = OrderListModel
        fields = ['order_no', 'cus_id', 'order_date', 'description', 'total_amount']

class NestOrderDetaislSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetailsModel
        fields = ['ordered_id', 'product_id', 'unit_ordered', 'price_ordered', 'quantity_ordered', 'total_amount_ordered']  

class NestCutomerDetailsSerializer(serializers.ModelSerializer):
    # order_details = NestOrderDetaislSerializer()
    # order_list = NestOrderListSerializer()
    class Meta:
        model = CustomerDetailsModel
        fields = [ 'cus_id', 'cus_name']  #, 'order_details', 'order_list'


# =====FOR POSTING DATA=======

class PostCutomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetailsModel
        fields = ['cus_id', 'cus_name', 'phone', 'address']

    def validate_cus_name(self, name):
        cus = CustomerDetailsModel.objects.filter(cus_name=name)
        if cus.exists():
            raise serializers.ValidationError('This Customer name is already exists!!!')
        return name   

class UpdateCutomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetailsModel
        fields = ['cus_id', 'cus_name', 'phone', 'address']

class PostUnitSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = UnitModel
        fields = ['product_id', 'unit_id', 'unit']

class PostProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['product_id', 'product_name', 'price']

    def validate_product_name(self, prod):
        prod_name = ProductModel.objects.filter(product_name=prod)
        if prod_name.exists():
            raise serializers.ValidationError('This product is already added !!!')
        return prod

class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['product_id', 'product_name', 'price']
        
class PostOrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetailsModel
        fields = ['ordered_id','order_id','product_id', 'unit_ordered', 'price_ordered', 'quantity_ordered', 'total_amount_ordered']  

class PostOrderListSerializer(serializers.ModelSerializer):   
    class Meta:
        model = OrderListModel
        fields = ['order_id', 'order_no', 'cus_id', 'order_date', 'description', 'total_amount']

    # def validate_total_amount(self, value):
    #     if int(value) <=0:
    #         raise serializers.ValidationError("Order Details can't be empty") 
    #     return value
    
# ========NEST DATE FOR ORDERLIST TABLE==========
# class TableCutomerNest(serializers.ModelSerializer):
#     customer_details = PostCutomerDetailsSerializer()
#     class Meta:
#         model = OrderListModel
# ====>

class TableOrderList(serializers.ModelSerializer):   
    class Meta:
        model = OrderListModel
        fields = ['order_no', 'order_date', 'description', 'total_amount']

class TableCutomerNest(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetailsModel
        fields = ['cus_id', 'cus_name'] # , 'order_list'

class TableOrderListSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    class Meta:
        model = OrderListModel
        fields = ['order_id', 'order_no', 'order_date', 'description', 'total_amount', 'cus_id', 'customer_name']

    def get_customer_name(self, obj):
        data = CustomerDetailsModel.objects.filter(cus_name=obj.cus_id).values()
        return data

class DataCount(serializers.ModelSerializer):
    iter_no = serializers.SerializerMethodField()
    class Meta:
        model = OrderListModel
        fields = [ 'order_id', 'iter_no']

    def get_iter_no(self, obj): 
            data = OrderListModel.objects.last()
            data_none = OrderListModel.objects.count()
            if data == []:
                return "OR0001" 
            else:       
                values = data.order_id + 1
                return "OR%004d" % values
    

class NestDetailsInList(serializers.ModelSerializer):
    order_details = serializers.SerializerMethodField()
    customer_details = serializers.SerializerMethodField()
    # product_details = serializers.SerializerMethodField()
    class Meta:
        model = OrderListModel
        fields = ['order_id', 'order_no', 'order_date', 'description', 'total_amount', 'cus_id', 'customer_details', 'order_details']

    def get_order_details(self, obj):
        data = OrderDetailsModel.objects.filter(order_id=obj.order_id).values()
        return data

    def get_customer_details(self, obj):
        cus = CustomerDetailsModel.objects.filter(cus_name=obj.cus_id).values()
        return cus

    # def get_product_details(self, obj):
    #     prod = ProductModel.objects.filter(product_name=obj.order_details[0].product_ordered).values()
    #     return prod

class UnitProdNest(serializers.ModelSerializer):
    product_id = PostProductSerializer()
    class Meta:
        model = UnitModel
        fields = ['unit_id', 'product_id', 'unit']

class NestProductInOrderDetailsSerializer(serializers.ModelSerializer):
    # product_details = serializers.SerializerMethodField()
    product_id = PostProductSerializer()
    class Meta:
        model = OrderDetailsModel
        fields = ['ordered_id', 'order_id', 'product_id', 'unit_ordered', 'price_ordered', 'quantity_ordered', 'total_amount_ordered', ]

    # def get_product_details(self, obj):
    #     data = ProductModel.objects.filter(product_id=obj.product_id_id).values()
    #     return data

class NestOrderDetailsInOrderSerizlizer(serializers.ModelSerializer):
    # order_details = NestProductInOrderDetailsSerializer(many=True)
    order_details = serializers.SerializerMethodField()
    class Meta:
        model = OrderListModel
        fields = ['order_id', 'order_details', 'order_no', 'cus_id', 'order_date', 'description', 'total_amount' ]

    def get_order_details(self, obj):
        data = OrderDetailsModel.objects.filter(order_id_id = obj.order_id).values()
        return data