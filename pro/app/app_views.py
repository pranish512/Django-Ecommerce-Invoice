from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import json
from django.db import transaction

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
    if_home = 1
    return render(request, 'home.html', {'customer':customer_details, 'order_details':order_details, 'order_list':order_list, 'product':product, 'unit':unit, 'order_no':order_no, 'home_page':if_home})

# @transaction.atomic
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
        
        # orderlist = requests.post('{url}postordlist/'.format(url=url), data=data)
        # status_code_list = [200, 302, 201]
        # if orderlist.status_code in status_code_list:
        try:
            array = request.POST['hiddenArray']
            print('ARRAYYYY$$$$$$$$$$$$$', array)   
            data_json = json.loads(array)
            # get_orderlist = requests.get('{url}postordlist/'.format(url=url)).json()
            
            with transaction.atomic():
                orderlist = requests.post('{url}postordlist/'.format(url=url), data=data)
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
                    "product_id":prod,
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
        except:
            messages.error(request, 'ADD product details!!!')
            return redirect('home')
    else:
        order_list  = requests.get('{url}nesttableorderlist/'.format(url=url)).json()
        print(order_list)
        return render(request, 'orderlist.html', {'order_list': order_list})

def orderupdates(request, id):
    if request.POST.get('btnSaveOrder','')=='SaveOrder1':
        validate_t_amount = request.POST['txtTotalAmt']
        if float(validate_t_amount) > 0.00: 

            # DELETING OLD DATA ::
            ord_list_del = requests.delete('{url}editordlist/{pk}/'.format(url=url, pk=id))
            # ord_details_del = requests.delete('{url}editorddetails/{pk}/'.format(url=url, pk=id))

            print(ord_list_del)
            # print(ord_details_del)

            # GETTING VALUE FROM TEMPLATE::
            # IF_VALUE FOR IF STATEMENT ::
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
                        "product_id":prod,
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
        else:
            messages.error(request, 'Invalid Credentials!!!')
            return redirect('orderlist')
                
    elif request.POST.get('hiddenPostEdit', '')=='editOrder1':
        if_value = request.POST['hiddenPostEdit']
        print('IF VALUE $$$$$$$$$$$$$$$$::::::::::::::', if_value)

        customer_details  = requests.get('{url}nestcusdetails/'.format(url=url)).json()
        orderlist = requests.get('{url}nestlist/{pk}/'.format(url=url, pk=id)).json()
        unit  = requests.get('{url}nestunit/'.format(url=url)).json()
        product  = requests.get('{url}nestprod/'.format(url=url)).json()
        # orderlist = requests.get('{url}editordlist/{pk}/'.format(url=url, pk=id)).json()
        return render(request, 'home.html', 
        {'customer': customer_details, 'orderlist':orderlist, 
        'if_true': if_value, 'product':product, 'unit':unit })
        # return JsonResponse( {'customer': customer_details, 'orderlist':orderlistnest})
    else:
        if_orderlist = 1
        table =requests.get('{url}postcusdetails/'.format(url=url)).json()
        return render(request, 'orderlist.html', {'orderlist_page': if_orderlist})

def remove(request, id):
    requests.delete('{url}editordlist/{pk}'.format(url=url, pk=id))
    messages.warning(request, 'Successfully Deleted!!!')
    return redirect('orderlist')

def addProductUnit(request):
    if request.POST.get('hiddenAddProd')=='addProd1':
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$ ITS PRODUCTTTT:::::')
        # key_val = request.POST['hiddenAddProd']
        prod_name = request.POST['txtProductName']
        price = request.POST['txtPrice']
        data = {
            'product_name':prod_name,
            'price':price,
        }
        print(data)
        addCustomer = requests.post('{url}postprod/'.format(url=url), data=data)
        status_code_list = [200, 302, 201]
        if addCustomer.status_code in status_code_list:
            messages.success(request, 'Successfully Saved!!!')
            return redirect('addProdUnit')
        else:
            print(addCustomer)
            messages.error(request, 'Invalid Credentials!!!')
            return redirect('addProdUnit')
    elif request.POST.get('hiddenAddUnit')=='addUnit1':
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$ ITS UNITTTTT:::::')
        prod_id = request.POST['ddlProductName']
        unit = request.POST['txtUnit']
        # unit = request.POST['ddlUnit']

        data = {
            'product_id':prod_id,
            'unit':unit,
        }

        print(data)
        addUnit = requests.post('{url}postunit/'.format(url=url), data=data)
        status_code_list = [200, 302, 201]
        if addUnit.status_code in status_code_list:
            messages.success(request, 'Successfully Saved!!!')
            return redirect('addProdUnit')
        else:
            print(addUnit)
            print(addUnit.text)
            messages.error(request, 'Invalid Credentials!!!')
            return redirect('addProdUnit')
    else:
        tableProd = requests.get('{url}nestprod/'.format(url=url)).json() 
        tableUnit = requests.get('{url}nestunit/'.format(url=url)).json()
        ddlProd = requests.get('{url}postprod'.format(url=url)).json()
        return render(request, 'addProductUnit.html', {'table':tableProd, 'tableUnit':tableUnit, 'product_name':ddlProd})

def removeproductdetail(request, id):
    if request.POST.get('btnProductDelete')=='DeleteProductDetails':
        requests.delete('{url}editprod/{pk}/'.format(pk=id, url=url))
        messages.warning(request, 'Successfully Deleted!!!')
        return redirect('addProdUnit')
    elif request.POST.get('btnUnitDelete')=='DeleteUnitDetails':
        requests.delete('{url}nestunit/{pk}/'.format(pk=id, url=url))
        messages.warning(request, 'Successfully Deleted!!!')
        return redirect('addProdUnit')
    # elif request.POST.get()
    else:    
        return redirect('addProdUnit')
    

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
            return redirect('addcustomer')
        else:
            print(addCustomer)
            messages.error(request, 'Customer creation failed!!!')
            cus_err = addCustomer.text
            print(cus_err)
            data = requests.get('{url}postcusdetails/'.format(url=url)).json
            return render(request, 'addCustomer.html', {'table':data, 'error':cus_err})
    else:
        data = requests.get('{url}postcusdetails/'.format(url=url)).json
        return render(request, 'addCustomer.html', {'table':data})


def masterUpdate(request, id):
    if request.POST.get('btnCustomerUpdate', '')=='updateCustomer1':
        print('ITSS CUSTOMERRRRRRRRRRR!!!!!!!!')  
        cus_name = request.POST['txtCustomerName']
        phone = request.POST['txtPhone']
        address = request.POST['txtAddress']
        data = {
            'cus_name':cus_name,
            'phone':phone,
            'address': address,
        }
        print(data)
        updateCus = requests.put('{url}editcusdetails/{pk}/'.format(url=url, pk=id), data=data)
        status_code_list = [200, 302, 201]
        if updateCus.status_code in status_code_list:
            messages.success(request, 'Successfully Updated!!!')
            return redirect('addcustomer')
        else:
            messages.error(request, 'Update Failed!!!')
            return redirect('addcustomer')
    elif request.POST.get('btnProductUpdate', '')=='updateProd1':
        print('ITSSS PRODUCT UPDATEEEEEEE!!!!!!!!!!!!!!!')
        prod_name = request.POST['txtProductName']
        price = request.POST['txtPrice']
        data = {
            'product_name':prod_name,
            'price':price,
        }
        editprod = requests.put('{url}editprod/{pk}/'.format(url=url, pk=id), data=data)
        status_code_list = [200, 302, 201]
        if editprod.status_code in status_code_list:
            messages.success(request, 'Successfully Updated!!!')
            return redirect('addProdUnit')
        else:
            messages.error(request, 'Update Failed!!!')
            return redirect('addProdUnit')
    elif request.POST.get('btnUnitUpdate', '')=='updateUnit1':
        print('ITSSS UNITTTTTTTTTTT $$$$$$$$$$$$$$$ UPDATEEEEEEE!!!!!!!!!!!!!!!')
        prod_id = request.POST['ddlProductName']
        unit = request.POST['txtUnit']
        data = {
            'product_id':prod_id,
            'unit':unit,  
        }
        editunit = requests.put('{url}editunit/{pk}/'.format(url=url, pk=id), data=data)
        status_code_list = [200, 302, 201]
        if editunit.status_code in status_code_list:
            messages.success(request, 'Successfully Updated!!!')
            return redirect('addProdUnit')
        else:
            messages.error(request, 'Update Failed!!!')
            return redirect('addProdUnit')
    else:        
        return redirect('home')

def removecustomerdetails(request, id):
    requests.delete('{url}editcusdetails/{pk}/'.format(pk=id, url=url))
    messages.warning(request, 'Successfully Deleted!!!')
    return redirect('addcustomer')