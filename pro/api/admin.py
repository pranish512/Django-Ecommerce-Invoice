from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomerDetailsModel)
admin.site.register(UnitModel)
admin.site.register(ProductModel)
admin.site.register(OrderDetailsModel)
admin.site.register(OrderListModel)