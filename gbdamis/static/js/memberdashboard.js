const user_phone =  $('#payment-phone-number').val()
$(document).on('click', '#pay-dues', function(e){
    console.log('pay dues clicked')
    $('#pay-dues-modal').modal('show')
    
    $('#change_number').on('click', function(e){
        e.preventDefault();
        $("#payment-phone-number").prop('disabled', false)
        $('#payment-phone-number').focus()
    })

    $('#payment-phone-number').on('change', function(e){
        $("#payment-phone-number").prop('disabled', true)
    })

    $(document).on('click', '.proceed-payment', function(e){
        const phone_number = $('#payment-phone-number').val()
        $.ajax({
            type: 'POST',
            url: '/pay-dues/',
            data: {
                'phone_number' : phone_number,
                'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
                },
            
            success: function(data){
                console.log(data)
                
            },
            error : function(xhr, errmsg, err){
                console.log(xhr.status + ' ' + xhr.responseText)
            }


        })

    })
    // $.ajax({
    //     type: 'GET',
    //     url: '/pay-dues/',
    //     data: {
    //         'name' : 'Name' 
    //         },
    //     success: function(data){
    //         console.log('success')
    //     },
    //     error : function(xhr, errmsg, err){
    //         console.log(xhr.status + ' ' + xhr.responseText)
    // }
    
    // })
})