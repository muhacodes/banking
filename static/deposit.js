$(document).ready(function(){

    disable_balance_field();
    // get_balance();
    calculateBalance();
    
});

function disable_balance_field(){

    $("#id_balance").prop("readonly", true);
}

function submit_button(){
    $("#btnSubmit").attr("disabled", true);
}

function calculateBalance(){
    $('#id_amount').keyup(function(){
        var id = $('#id_client').children("option:selected").val();
        get_balance(id);
        
    });
}

function get_balance(id){
    var amount = 0;

    $.ajax({
        url: '/transactions/transactions/'+id+' ',
        contentType: "application/json; charset=utf-8",
        
        dataType: 'json',
        success: function (response) {
            // alert(response.amount);
            var total_amount = $('#id_amount').val();
            if($.isNumeric(response.amount)){

                amount = parseInt(response.amount) + parseInt(total_amount);

            }
            
            // alert(total_amount);
            // alert(amount);
            // alert(amount);
            $('#id_balance').val(amount);
        }
    });
}