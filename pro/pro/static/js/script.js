

// AJAX FOR ORDER-NUMBER BINDING::::

$(document).ready(function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/orderno/',
        method: 'GET',
        data: '',
        dataType: 'json',

    }).done(function (data) {
        $('#txtOrderNo').val(data[0].iter_no)
    })
})


// TIMEOUT FOE MESSAGES
setTimeout(() => {
    if ($('#divMsg').length > 0) {
        $('#divMsg').remove();
    }
}, 2500);


// ORDER LIST EDIT PAGE --2 ::
function editOrder(x) {
    alert(x)
    $.ajax({
        url: 'http://127.0.0.1:8000/api/nesttableorderlist/' + x + '/',
        method: 'GET',
        data: '',
        dataType: 'json',
    }).done(function (data) {
        alert('data get done')
        $('#ddlCustomer').val(data.customer_name[0].cus_id);
        $('#txtOrderNo').val(data.order_no);
        $('#txtOrderDate').val(data.order_date);
        $('#txtDescription').val(data.description);
        $('#txtTotalAmt').val(data.total_amount);
        console.table(data.cus_id, data.order_no, data.order_date, data.description, data.total_amount)
    });
};



var sno = 0;
var x = document.getElementById("btnAddProduct");
var y = document.getElementById("btnUpdateProduct");
if (x && y) {
    x.style.display = "block";
    y.style.display = "none";
}

// AUTOMATIC TOTALING PRICE + AMOUNT + UNIT ::::

$(document).ready(function () {
    var tableOrder = document.getElementById("tableAddProduct");
    var totalAmount = 0;
    var totalPrice = 0;
    var totalQuantity = 0;
    for (var k = 1; k < tableOrder.rows.length - 1; k++) {
        totalPrice = totalPrice + parseFloat(tableOrder.rows[k].cells[3].textContent);
        totalQuantity = totalQuantity + parseFloat(tableOrder.rows[k].cells[4].textContent);
        totalAmount = totalAmount + parseFloat(tableOrder.rows[k].cells[5].textContent);
    }

    document.getElementById("txtTotalPrice").innerHTML = parseFloat(totalPrice).toFixed(2);
    document.getElementById("txtTotalQty").innerHTML = parseFloat(totalQuantity);
    document.getElementById("txtTableTotalAmt").innerHTML = parseFloat(totalAmount).toFixed(2);
    document.getElementById("txtTotalAmt").value = parseFloat(totalAmount).toFixed(2);

})

// TOTALING PRICE + AMOUNT + UNIT ::::

function findTotalSum() {
    var tableOrder = document.getElementById("tableAddProduct");
    var totalAmount = 0;
    var totalPrice = 0;
    var totalQuantity = 0;
    for (var k = 1; k < tableOrder.rows.length - 1; k++) {
        totalPrice = totalPrice + parseFloat(tableOrder.rows[k].cells[3].textContent);
        totalQuantity = totalQuantity + parseFloat(tableOrder.rows[k].cells[4].textContent);
        totalAmount = totalAmount + parseFloat(tableOrder.rows[k].cells[5].textContent);
    }

    document.getElementById("txtTotalPrice").innerHTML = parseFloat(totalPrice).toFixed(2);
    document.getElementById("txtTotalQty").innerHTML = parseFloat(totalQuantity);
    document.getElementById("txtTableTotalAmt").innerHTML = parseFloat(totalAmount).toFixed(2);
    document.getElementById("txtTotalAmt").value = parseFloat(totalAmount).toFixed(2);
}


// DELETE PRODUCT TABLE::::
function DeleteProduct(rowId) {
    document.getElementById("rowIndex" + rowId).remove();
    var table = document.getElementById('tableBodyID');
    var trow = table.rows.length;
    sno--;
    findTotalSum()

}

// UPDATE PRODUCT TABLE::::
function UpdateProduct() {
    var x = document.getElementById("btnAddProduct");
    var y = document.getElementById("btnUpdateProduct");
    x.style.display = "block";
    y.style.display = "none";
    var currentRow = document.getElementById("updateRow").innerText;
    console.log("currentRow", currentRow)
    var product1 = document.getElementById("ddlProductName");
    var product = product1.options[product1.selectedIndex].text;
    var productValue = document.getElementById("ddlProductName").value;
    console.log("product 1 ::", product1);
    console.log("product ::", product);
    console.log("productValue ::", productValue);

    document.getElementById("ddlProductName").value = product;
    document.getElementById("tdProd" + currentRow).innerHTML = product;
    document.getElementById("tdUnit" + currentRow).innerHTML = document.getElementById("txtUnit").value;
    document.getElementById("tdPrice" + currentRow).innerHTML = document.getElementById("txtPrice").value;
    document.getElementById("tdQty" + currentRow).innerHTML = document.getElementById("txtQuantity").value;
    document.getElementById("tdAmt" + currentRow).innerHTML = document.getElementById("txtAmount").value;

    findTotalSum()

    // UPDATING TO INPUT VALUES::::
    $('#ddlProductName').val('0');
    $('#txtUnit').val('');
    $('#txtPrice').val('');
    $('#txtQuantity').val('');
    $('#txtAmount').val('');
}

// EDIT PRODUCT TABLE:::::
function EditProduct(sno, pv) {
    console.log('args', sno, pv)
    // alert('ROWWWW', pv)
    // alert('SNOooo', sno)

    document.getElementById("ddlProductName").value = pv;
    document.getElementById("txtUnit").value = document.getElementById("tdUnit" + sno).innerText;
    document.getElementById("txtPrice").value = document.getElementById("tdPrice" + sno).innerText;
    document.getElementById("txtQuantity").value = document.getElementById("tdQty" + sno).innerText;
    document.getElementById("txtAmount").value = document.getElementById("tdAmt" + sno).innerText;
    // if (isNaN(pv)) {
    //     var product1 = document.getElementById("ddlProductName");
    //     product1.options[product1.selectedIndex].text = pv;
    //     document.getElementById("txtUnit").value = document.getElementById("tdUnit" + sno).innerText;
    //     document.getElementById("txtPrice").value = document.getElementById("tdPrice" + sno).innerText;
    //     document.getElementById("txtQuantity").value = document.getElementById("tdQty" + sno).innerText;
    //     document.getElementById("txtAmount").value = document.getElementById("tdAmt" + sno).innerText;
    // } else {
    //     document.getElementById("ddlProductName").value = pv;
    //     document.getElementById("txtUnit").value = document.getElementById("hiddenUnit" + sno).value;
    //     document.getElementById("txtPrice").value = document.getElementById("hiddenPrice" + sno).value;
    //     document.getElementById("txtQuantity").value = document.getElementById("hiddenQty" + sno).value;
    //     document.getElementById("txtAmount").value = document.getElementById("hiddenAmt" + sno).value;
    // }

    x.style.display = "none";
    y.style.display = "block";
    document.getElementById("updateRow").innerText = sno;

}

// ADD PRODUCT TO TABLE:::::
function AddProduct() {
    // alert('ADD ')
    sno++;
    let tableIndex = "hiddentd" + sno;
    var table = document.getElementById("tableAddProduct");
    var table_len = (table.rows.length) - 1;
    var product1 = document.getElementById("ddlProductName");
    var product = product1.options[product1.selectedIndex].text;
    // var product = document.getElementById("ddlProductName").value;
    var productValue = document.getElementById("ddlProductName").value;
    var unit = document.getElementById("txtUnit").value;
    var price = document.getElementById("txtPrice").value;
    var quantity = document.getElementById("txtQuantity").value;
    var amount = document.getElementById("txtAmount").value;
    var productDetails = [];
    // console.log(tableIndex, product, unit, price, quantity, amount)
    var table = document.getElementById('tableBodyID');
    var trow = table.rows.length;
    if (trow > 0) {
        // alert('TROW ID FUNCTING')
        trow++;
        $('#tableAddProduct').append('<tr id=' + "rowIndex" + trow + '><td id=' + "tableIndex" + trow + '><input type="hidden" name="hiddenSno" id="hiddenSno">' + trow +
            '</td><td role="'+ productValue +'" class="text-center" id=' + "tdProd" + trow + '><input type="hidden" name="hiddenProdID" id=' + "hiddenProdID" + trow + ' value=' + productValue + ' ><input type="hidden" name="hiddenProd" id=' + "hiddenProd" + trow + ' value=' + product + ' >' + product +
            '</td><td class="text-center" id=' + "tdUnit" + trow + '><input type="hidden" name="hiddenUnit" id=' + "hiddenUnit" + trow + ' value=' + unit + '>' + unit +
            '</td><td class="text-center" id=' + "tdPrice" + trow + '><input type="hidden" name="hiddenPrice" id=' + "hiddenPrice" + trow + ' value=' + price + '>' + price +
            '</td><td class="text-center" id=' + "tdQty" + trow + '><input type="hidden" name="hiddenQty" id=' + "hiddenQty" + trow + ' value=' + quantity + '>' + quantity +
            '</td><td class="text-center" id=' + "tdAmt" + trow + '><input type="hidden" name="hiddenAmt" id=' + "hiddenAmt" + trow + ' value=' + amount + '>' + amount +
            '</td><td><input type="button" name="btnEditProd" id="btnEditProd" onclick=EditProduct("' + trow + '","' + productValue + '") class="btn btn-success" value="Edit" >' +
            '</td><td><input type="button" class="btn btn-danger" value="Delete" onclick=DeleteProduct("' + trow + '") name="btnDeleteProd" id="btnDeleteProd"></td></tr>');
        productDetails.push()
    }else {
        // alert('SNO ID FUNCTING')
        $('#tableAddProduct').append('<tr id=' + "rowIndex" + sno + '><td id=' + "tableIndex" + sno + '><input type="hidden" name="hiddenSno" id="hiddenSno">' + sno +
            '</td><td role="'+ productValue +'" class="text-center" id=' + "tdProd" + sno + '><input type="hidden" name="hiddenProdID" id=' + "hiddenProdID" + sno + ' value=' + productValue + ' ><input type="hidden" name="hiddenProd" id=' + "hiddenProd" + sno + ' value=' + product + ' >' + product +
            '</td><td class="text-center" id=' + "tdUnit" + sno + '><input type="hidden" name="hiddenUnit" id=' + "hiddenUnit" + sno + ' value=' + unit + '>' + unit +
            '</td><td class="text-center" id=' + "tdPrice" + sno + '><input type="hidden" name="hiddenPrice" id=' + "hiddenPrice" + sno + ' value=' + price + '>' + price +
            '</td><td class="text-center" id=' + "tdQty" + sno + '><input type="hidden" name="hiddenQty" id=' + "hiddenQty" + sno + ' value=' + quantity + '>' + quantity +
            '</td><td class="text-center" id=' + "tdAmt" + sno + '><input type="hidden" name="hiddenAmt" id=' + "hiddenAmt" + sno + ' value=' + amount + '>' + amount +
            '</td><td><input type="button" name="btnEditProd" id="btnEditProd" onclick=EditProduct("' + sno + '","' + productValue + '") class="btn btn-success" value="Edit" >' +
            '</td><td><input type="button" class="btn btn-danger" value="Delete" onclick=DeleteProduct("' + sno + '") name="btnDeleteProd" id="btnDeleteProd"></td></tr>');
        productDetails.push()
    }

    findTotalSum()

    $('#ddlProductName').val('0');
    $('#txtUnit').val('');
    $('#txtPrice').val('');
    $('#txtQuantity').val('');
    $('#txtAmount').val('');
    x.style.display = "block";
    y.style.display = "none";
}


// DATE USING JS::::::
function loaddate() {
    var now = new Date();
    var year = now.getFullYear();
    var month = now.getMonth() + 1;
    var days = now.getDate();
    var hrs = now.getHours();
    var min = now.getMinutes();
    var seconds = now.getSeconds();
    var today = days + "-" + month + "-" + year; // + ", Time-" + hrs + "h-" + min + "m-" + seconds + 's';

    $('#txtOrderDate').val(today)
    console.log(today)
}

//==========================PRODUCT DROP DOWN=============================

$('#ddlProductName').change(function () {
    var id = $('#ddlProductName').val();

    $.ajax({
        url: 'http://127.0.0.1:8000/api/nestprod/' + id + '/',
        method: 'GET',
        data: '',
    }).done(function (data) {
        $.each(data, function () {
            //const obj = Object.entries(index)
            //console.log(Object.fromEntries(obj))  
            $('#txtUnit').val(data.units[0].unit);
            $('#txtPrice').val(data.price);
        })
    })
})

// AMOUNT CALCULATION
function CalculateAmount(value) {
    var price = $('#txtPrice').val()
    $('#txtAmount').val(parseFloat(value * price).toFixed(2));
};

// ADD PRODUCT TO TABLE

function validateAddProduct() {
    let product = document.getElementById('ddlProductName').value;
    let quantity = document.getElementById('txtQuantity').value;

    if (product == "0") {
        alert('Choose Product!!!');
        return false;
    }
    if (quantity == "") {
        alert('Choose Quantity!!!');
        $('#txtQuantity').attr('style', 'background: #ffe6ee; border: 1px solid #df1b1b; box-shadow: 1px 1px 12px 1px #df1b1b;')
        setTimeout(() => { if ($('#txtQuantity').length > 0) { $('#txtQuantity').attr('style', 'disabled'); } }, 2500)
        return false;
    }
    else {
        AddProduct()
    }

}

// VALIDATING SAVE ORDER AND GETTING TABLE VALUES TO ARRAY::
function validateForm() {
    var cus = document.getElementById('ddlCustomer').value;
    if (cus == "0") {
        alert("Select customer name!!!");
        return false;
    }

    var table = document.getElementById('tableBodyID');
    var trow = table.rows.length;
    if (trow <= 0) {
        alert("Add products to save order!!!")
        return false;
    }

    // var amt = document.getElementById('txtTotalAmt').value;
    // if (amt <0) {
    //     alert("Total amount must be filled out!!!");
    //     return false;
    // }

    // var desp = document.getElementById('txtDescription').value;
    // if (desp == "") {
    //     alert("Description must be filled out!!!");
    //     return false;
    // }

    var productDetails = [];

    //gets table
    var prodTable = document.getElementById('tableAddProduct');

    //gets rows of table
    var rowLength = prodTable.rows.length;
    console.log("ROW LENGTHHH:::;;; ", rowLength);

    for (var i = 1; i < rowLength - 1; i++) {
        var prodCells = prodTable.rows.item(i).cells;
   
        var dataVal = {
            // 'product_ordered': document.getElementById('hiddenProdID' + i).value, // .find('input[type=hidden]')
            'product_ordered': prodCells.item(1).role,
            'unit_ordered': prodCells.item(2).textContent,
            'price_ordered': prodCells.item(3).textContent,
            'quantity_ordered': prodCells.item(4).textContent,
            'total_amount_ordered': prodCells.item(5).textContent,
        }
        productDetails.push(dataVal);
    }
    console.log(productDetails);
    var orderNumber = document.getElementsByName('txtOrderNo').value;
    var finalOrderList = {
        "order_no": orderNumber,
        "productDetails": productDetails
    }
    console.log("FINALE ORDER LIST::", finalOrderList)
    // str_data =  JSON.stringify(finalOrderList)
    str_prod_data = JSON.stringify(productDetails)
    $("#hiddenArray").val(str_prod_data);


}


function sideBarDD() {
    var menu = document.getElementById('sub-menu');
    var DDbtn = document.getElementById('sidebarDDbtn');
    var i;
    // for (i = 0; i < DDbtn.length; i++) {
    //     DDbtn[i].addEventListener("click", function () {
    //         this.classList.toggle("active");
    if (menu.style.display == 'none') {
        menu.style.display = "block";
    } else {
        menu.style.display = 'none';
    }
    //     });
    // }
}

// Product Name Binding Using ID::::
let ifIdInput = $('#hiddenProdID1').val()
var tableOrder = document.getElementById("tableAddProduct");
if (ifIdInput != '') {
    console.log(ifIdInput)
    for (var b = 1; b < tableOrder.rows.length - 1; b++) {
        let idInput = $('#hiddenProdID' + b).val()
        let loopCounter = $('#hiddenLoopCounter' + b).val()
        console.table('PRODUCT ID:::', idInput, loopCounter)
        $.ajax({
            url: 'http://127.0.0.1:8000/api/nestprod/' + idInput + '/',
            method: 'GET',
            data: '',
            dataType: 'json',
        }).done((data) => {
            console.log(data)
            $('#tdProd' + loopCounter).text(data.product_name)
        })
    }
}


// var dropdown = document.getElementsByClassName("dropdown-btn");
// var i;

// for (i = 0; i < dropdown.length; i++) {
//     dropdown[i].addEventListener("click", function () {
//         this.classList.toggle("active");
//         var dropdownContent = this.nextElementSibling;
//         if (dropdownContent.style.display === "block") {
//             dropdownContent.style.display = "none";
//         } else {
//             dropdownContent.style.display = "block";
//         }
//     });
// }

