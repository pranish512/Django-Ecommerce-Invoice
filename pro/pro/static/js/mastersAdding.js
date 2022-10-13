
setTimeout(function () { if ($('#divErrorCode').length > 0) { $('#divErrorCode').remove(); } }, 4000)

function EditCustomerDetails(x){
    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/editcusdetails/'+ x +'/',
        data: '',
        dataType: 'json',
    }).done(function(data){
        console.log(data)
        $('#txtCustomerName').val(data.cus_name);
        $('#txtPhone').val(data.phone);
        $('#txtAddress').val(data.address);  
        $('#formAddCustomer').attr('action', '/masterupdate/'+ x +'/' );
        $('#btnCustomerUpdate').attr('style', '');
        $('#btnCustomerSave').attr('style', 'display: None;');
    })
}

function EditProductDetails(x){
    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/nestprod/'+ x +'/',
        data: '',
        dataType: 'json',
    }).done(function(data){
        console.log(data)
        $('#txtProductName').val(data.product_name);
        $('#txtPrice').val(data.price);
        $('#txtUnit').val(data.units[0].unit);
        $('#ddlProductName').val(data.units[0].product_id);
        $('#formAddProduct').attr('action', '/masterupdate/'+ x +'/' );
        y = data.units[0].unit_id
        $('#formAddUnit').attr('action', '/masterupdate/'+ y +'/' );
        $('#btnUnitUpdate').attr('style', '');
        $('#btnProductUpdate').attr('style', '');
        $('#btnProductSave').attr('style', 'display: None;');
        $('#btnUnitSave').attr('style', 'display: None;');
    })  
}

// function EditUnitDetails(y){
//     $.ajax({
//         method: 'GET',
//         url: 'http://127.0.0.1:8000/api/editunit/'+ y +'/', 
//         data: '',
//         dataType: 'json',
//     }).done(function(data){
//         console.log(data)
//         $('#txtUnit').val(data.unit);
//         $('#formAddUnit').attr('action', '/masterupdate/'+ y +'/' );
//         $('#btnUnitUpdate').attr('style', '');
//         $('#btnUnitSave').attr('style', 'display: None;');
//     })  
// }

function SaveProductValidation(){
    var prod = $('#txtProductName').val();
    // var prod = document.getElementById('txtProductName').value; 
    var price = document.getElementById('txtPrice').value;
    if (prod == ''){
        alert('Product name field should be filled!!!');
        return false;
    }
    if (price == ''){
        alert('Add Price to the product!!!')
        return false;
    }
}

function SaveCustomerValidation(){  
    var name = document.getElementById('txtCustomerName').value;
    if (name == ''){
        alert('Customer Name is empty!!!');
        return false;
    }
    var phone = document.getElementById('txtPhone').value;
    if (phone == ''){
        alert('Phone number should be added!!!');
        return false;
    }
    var address = document.getElementById('txtAddress').value;
    if (address == ''){
        alert('Add customer address!!!');
        return false;
    }
      // if (phone > 13 ){
    //     alert('Enter correct phonenumber!!!')
    //     return false;
    // }
    // if (isNaN(phone)){
    //     alert('Enter valid phone number!!!');
    //     return false;
    // }

}

function SaveUnitValidation(){
    var prod = document.getElementById('ddlProductName').value;
    var unit = document.getElementById('txtUnit').value; 
    if (prod=='0'){
        alert('Select the product!!!');
        return false;
    }
    if (unit==''){
        alert('Enter Unit of the product!!!')
        return false;
    }
}