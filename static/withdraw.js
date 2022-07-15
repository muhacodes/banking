$(document).ready(function(){

    // alert('withdraw');
    disable_balance_field();
    // get_balance();
    calculateBalance();
    submit_button();
    $( "#id_amount" ).change(function() {
        // alert( "Handler for .change() called." );
      });
    
});

function disable_balance_field(){

    $("#id_balance").prop("readonly", true);
}

function submit_button(){
    $("#submit_button").attr("disabled", true);
}



function calculateBalance(){
    $('#id_amount').change(function(){
        var id = $('#id_client').children("option:selected").val();
        var balance  = get_balance(id);
        var amount = $('#id_amount').val();
        // if(parseInt(balance) > parseInt(amount)){
        //     $("#submit_button").attr("disabled", false);
        // }

        // get_balance(id);

        var current_balance = $('#id_balance').val();
        alert(current_balance);
        if(current_balance > 0) {
            $("#submit_button").removeAttr("disabled");
        }else{
            $("#submit_button").attr("disabled", true);
        }
        // if(parseInt($('#id_balance').val() >= 0)){
        //     alert('more than zero');
        //     
        // }
        
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
            if($.isNumeric(response.amount) && $.isNumeric(total_amount) ){

                amount = parseFloat(response.amount) - parseFloat(total_amount);
            }
            // alert(total_amount);
            // alert(amount);
            $('#id_balance').val(amount);
        }
    });

    return amount;
    
}