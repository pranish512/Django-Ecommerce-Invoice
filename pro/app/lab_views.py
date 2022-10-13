from array import array
from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import json

url = settings.URL

# Create your views here.

def home(request):
    customer_details  = requests.get('{url}nestcusdetails/'.format(url=url)).json()
    order_details  = requests.get('{url}nestorddetails/'.format(url=url)).json()
    order_list  = requests.get('{url}nestordlist/'.format(url=url)).json()
    unit  = requests.get('{url}nestunit/'.format(url=url)).json()
    product  = requests.get('{url}nestprod/'.format(url=url)).json()
    order_no = requests.get('{url}orderno/'.format(url=url)).json()
    print(order_no)

    return render(request, 'home.html', {'customer':customer_details, 'order_details':order_details, 'order_list':order_list, 'product':product, 'unit':unit, 'order_no':order_no})

def orderlist(request):
    if request.method == 'POST':
        customer_id = request.POST['ddlCustomer'] 
        ord_no = request.POST['txtOrderNo']
        ord_date = request.POST['txtOrderDate']
        description = request.POST['txtDescription']
        total_amount = request.POST['txtTotalAmt']

        data = {
            'order_no':ord_no,
            'cus_id':customer_id,
            'order_date': ord_date,
            'description': description,
            'total_amount': total_amount,
        }
        # print(data)
        
        orderlist = requests.post('{url}postordlist/'.format(url=url), data=data)
        status_code_list = [200, 302, 201]
        if orderlist.status_code in status_code_list:
            array = request.POST['hiddenArray']
            print('ARRAYYYY$$$$$$$$$$$$$', array)   
            data_json = json.loads(array)
            # get_orderlist = requests.get('{url}postordlist/'.format(url=url)).json()
            value = orderlist.text
            json_data = json.loads(value)
            print('POST ORDER TYPEEEEEEEE$$$$$$$$$$$$:::::::::', type(json_data))
            print('POST ORDER LISR RESPONSE::', json_data)
            # print('POST ORDER GETTTING ORDER_IDD::::::', json_data['order_id'])
            get_order_id = json_data['order_id']

            for arr in data_json:
                # print(arr)
                prod = arr['product_ordered']
                unit = arr['unit_ordered']
                price = arr['price_ordered']
                qty = arr['quantity_ordered']
                t_amt = arr['total_amount_ordered']
                # print(prod, unit, price, qty, t_amt)
                table_data = {
                    "order_id":get_order_id,
                    "product_ordered":prod,
                    "unit_ordered":unit,
                    "price_ordered":price,
                    "quantity_ordered":qty,
                    "total_amount_ordered":t_amt,
                }
                print(table_data)
                table_post_response = requests.post('{url}postorddetails/'.format(url=url), data=table_data) 
                print(table_post_response)    
            
            status_code_list = [200, 302, 201]
            if orderlist.status_code in status_code_list:
                messages.success(request, 'Successfully Saved!!!')
                return redirect('orderlist')
            else:
                print(orderlist)
                messages.error(request, 'Something Went Wrong!!!')
                return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials!!!')
            return redirect('home')
    else:
        order_list  = requests.get('{url}nesttableorderlist/'.format(url=url)).json()
        print(order_list)
        return render(request, 'orderlist.html', {'order_list': order_list})

def orderupdates(request, id):
    if request.POST.get('btnSaveOrder','')=='SaveOrder1':

        # DELETING OLD DATA ::
        ord_list_del = requests.delete('{url}editordlist/{pk}/'.format(url=url, pk=id))
        # ord_details_del = requests.delete('{url}editorddetails/{pk}/'.format(url=url, pk=id))

        print(ord_list_del)
        # print(ord_details_del)

        # GETTING VALUE FROM TEMPLATE::]

        # GETTING IF_VALUE FOR IF STATEMENT ::
        if_value = request.POST['btnSaveOrder']
        print('THIS ISSS FOR UPDATE POST:::::', if_value )

        # DETAILS FOR ORDER LIST ::
        customer_id = request.POST['ddlCustomer'] 
        ord_no = request.POST['txtOrderNo']
        ord_date = request.POST['txtOrderDate']
        description = request.POST['txtDescription']
        total_amount = request.POST['txtTotalAmt']

        data = {
            'order_no':ord_no,
            'cus_id':customer_id,
            'order_date': ord_date,
            'description': description,
            'total_amount': total_amount,
        }

        print(data)
        edit_order_list = requests.post('{url}postordlist/'.format(url=url), data=data)
        status_code_list = [200, 302, 201]
        if edit_order_list.status_code in status_code_list:
            # GETTING HIDDEN ARRAY FROM JS TABLE
            array = request.POST['hiddenArray']
            print('ARRAYYYY$$$$$$$$$$$$$', array)  
            data_json = json.loads(array)
            # GETTING ORDER_ID FOR SAVING ORDER_DETAILS UNDER THEM FOR FUTURE NESTING PURPOSE
            value = edit_order_list.text
            json_data = json.loads(value)
            get_order_id = json_data['order_id']

            # USING FOR LOOP FOR SEPARATE ARRAY DATA::
            for arr in data_json:
                prod = arr['product_ordered']
                unit = arr['unit_ordered']
                price = arr['price_ordered']
                qty = arr['quantity_ordered']
                t_amt = arr['total_amount_ordered']
                table_data = {
                    "order_id":get_order_id,
                    "product_ordered":prod,
                    "unit_ordered":unit,
                    "price_ordered":price,
                    "quantity_ordered":qty,
                    "total_amount_ordered":t_amt,
                }
                print(table_data)

                # POST THE ORDER DETAIS DATA
                table_post_response = requests.post('{url}postorddetails/'.format(url=url), data=table_data) 
                # print(table_post_response)
            status_code_list = [200, 302, 201]    
            if table_post_response.status_code in status_code_list:
                messages.success(request, 'Successfully Saved!!!')
                return redirect('orderlist')
            else:
                print(table_post_response)
                print(table_post_response.text)
                messages.error(request, 'Invalid Credentials!!!')
                return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials!!!')
            return redirect('home')
            
    elif request.POST.get('hiddenPostEdit', '')=='editOrder1':
        if_value = request.POST['hiddenPostEdit']
        print('IF VALUE $$$$$$$$$$$$$$$$::::::::::::::', if_value)

        customer_details  = requests.get('{url}nestcusdetails/'.format(url=url)).json()
        orderlistnest = requests.get('{url}nestlist/{pk}/'.format(url=url, pk=id)).json()
        unit  = requests.get('{url}nestunit/'.format(url=url)).json()
        product  = requests.get('{url}nestprod/'.format(url=url)).json()
        # orderlist = requests.get('{url}editordlist/{pk}/'.format(url=url, pk=id)).json()
        print(orderlistnest)
        return render(request, 'home.html', {'customer': customer_details, 'orderlist':orderlistnest, 'if_true': if_value, 'product':product, 'unit':unit })
        # return JsonResponse( {'customer': customer_details, 'orderlist':orderlistnest})
    else:
        return render(request, 'orderlist.html')

def remove(request, id):
    requests.delete('{url}editordlist/{pk}'.format(url=url, pk=id))
    messages.warning(request, 'Successfully Deleted!!!')
    return redirect('orderlist')

def masterpage(request):
    product_name = requests.get('{url}postprod/'.format(url=url)).json()
    return render(request, 'masters.html', {'product_name':product_name})

def addCustomers(request):
    if request.method == 'POST':
        cus_name = request.POST['txtCustomerName']
        phone = request.POST['txtPhone']
        address = request.POST['txtAddress']
        data = {
            'cus_name':cus_name,
            'phone':phone,
            'address': address,
        }
        print(data)
        addCustomer = requests.post('{url}postcusdetails/'.format(url=url), data=data)
        status_code_list = [200, 302, 201]
        if addCustomer.status_code in status_code_list:
            messages.success(request, 'Successfully Saved!!!')
            return redirect('master')
        else:
            print(addCustomer)
            messages.error(request, 'Invalid Credentials!!!')
            return redirect('master')
    else:
        return render(request, 'masters.html')

def addProducts(request):
    if request.method == 'POST':
        prod_name = request.POST['txtProductName']
        # unit = request.POST['ddlUnit']
        price = request.POST['txtPrice']
        data = {
            'product_name':prod_name,
            'price':price,
            # 'cus_name':cus_name,
        }
        print(data)
        addCustomer = requests.post('{url}postprod/'.format(url=url), data=data)
        status_code_list = [200, 302, 201]
        if addCustomer.status_code in status_code_list:
            messages.success(request, 'Successfully Saved!!!')
            return redirect('master')
        else:
            print(addCustomer)
            messages.error(request, 'Invalid Credentials!!!')
            return redirect('master')
    else:
        return render(request, 'masters.html')

def addUnits(request):
    if request.method == 'POST':
        prod_id = request.POST['ddlProductName']
        # unit = request.POST['ddlUnit']
        unit = request.POST['txtUnit']
        data = {
            'product_id':prod_id,
            'unit':unit,
            # 'cus_name':cus_name,
        }
        print(data)
        addUnit = requests.post('{url}postunit/'.format(url=url), data=data)
        status_code_list = [200, 302, 201]
        if addUnit.status_code in status_code_list:
            messages.success(request, 'Successfully Saved!!!')
            return redirect('master')
        else:
            print(addUnit)
            print(addUnit.text)
            messages.error(request, 'Invalid Credentials!!!')
            return redirect('master')
    else:
        return render(request, 'masters.html')
