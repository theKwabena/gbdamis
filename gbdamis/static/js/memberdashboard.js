const user_phone =  $('#payment-phone-number').val()
let otp ='';

function OTPInput() {
    const inputs = document.querySelectorAll('#otp > *[id]');
    const inputValues = []; // Array to store the input values
  
    for (let i = 0; i < inputs.length; i++) {
      inputs[i].addEventListener('keydown', function(event) {
        if (event.key === "Backspace") {
          inputs[i].value = '';
          if (i !== 0) {
            inputs[i - 1].focus();
          }
        } else {
          if (i === inputs.length - 1 && inputs[i].value !== '') {
            return true;
          } else if (event.keyCode > 47 && event.keyCode < 58) {
            inputs[i].value = event.key;
            if (i !== inputs.length - 1) {
              inputs[i + 1].focus();
            }
            event.preventDefault();
          } else if (event.keyCode > 64 && event.keyCode < 91) {
            inputs[i].value = String.fromCharCode(event.keyCode);
            if (i !== inputs.length - 1) {
              inputs[i + 1].focus();
            }
            event.preventDefault();
          }
        }
        // Store the input value in the array
      inputValues[i] = inputs[i].value;
      otp = inputValues.join('');

      });
    }
    
  }
  

  
const handle_otp = function(otp){
    // change confirm button text to verfiy otp
    $('.modal-form').html(
        
        "<form  method='POST'>" + 
        '<p class="mb-3 text-center font-size-15">Enter the OTP sent to ' + '<span class="fw-bolder">' + user_phone + '</span>' + '</p>' +
        '<div id="otp" class="inputs d-flex flex-row justify-content-center mt-2">' +
            '<input class="m-2 text-center form-control rounded" type="text" id="first" maxlength="1" />' +
            '<input class="m-2 text-center form-control rounded" type="text" id="second" maxlength="1" />' +
            '<input class="m-2 text-center form-control rounded" type="text" id="third" maxlength="1" />' +
            '<input class="m-2 text-center form-control rounded" type="text" id="fourth" maxlength="1" />' +    
            '<input class="m-2 text-center form-control rounded" type="text" id="fifth" maxlength="1" />' +    
            '<input class="m-2 text-center form-control rounded" type="text" id="six" maxlength="1" />' +    
        '</div>' +
        '<div class="mb-3 d-flex justify-content-center">' + 
           '<p href="#" id="change_number">No OTP? click <span> <a href="#" class="text-primary fw-bolder"> here </a>  </span> to resend otp number </p>' + 
        '</div>' +
        '<div class="d-flex justify-content-center">' +
        '<button type="button" class="btn btn-light mt-3 mx-2" data-bs-dismiss="modal" aria-label="Close">Cancel</button>'
        + 
        '<button type="button" class="btn btn-danger mt-3 mx-2  proceed-payment">Verify OTP</button>' +

        '<div class="spinner-border text-success mx-2 my-n3 d-none" id="payment-loader" role="status">' + 
            '<span class="sr-only">Loading...</span>' + 
        '</div></div></form>'
    )
    OTPInput();

}
$(document).on('click', '#pay-dues', function(e){
    console.log('pay dues clicked')
    $('#pay-dues-modal').modal('show')
    // handle_otp()
    
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
        $(this).hide()
        $('#payment-loader').removeClass('d-none')
        console.log(phone_number)
        $.ajax({
            type: 'POST',
            url: '/pay-dues/',
            data: {
                'phone_number' : phone_number,
                'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
                },
            
            success: function(response){
                $('#payment-loader').addClass('d-none')
                $('.proceed-payment').show()
                handle_otp()
                console.log(response)
                if (response.status){
                    
                } else {
                   
                    console.log(response.message)
                    if (response.message){
                        $('#payment-phone-number').addClass('is-invalid')
                        if ($('#payment-phone-number').next().hasClass('invalid-feedback')){
                            $('.invalid-feedback').remove()
                            $("#payment-phone-number").after("<p class='invalid-feedback'> <strong> Please check phone number and try again</strong> </p>")
                        } else {
                            $("#payment-phone-number").after("<p class='invalid-feedback mt-n3'> <strong>Please check phone number and try again</strong> </p>")
                        }
                        $("#payment-phone-number").prop('disabled', false)

                    }

                }
                
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