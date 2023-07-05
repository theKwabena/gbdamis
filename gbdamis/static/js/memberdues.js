const user_phone =  $('#payment-phone-number').val()
let otp ='';
let amount = '';
let dues_id = '';
let payment_reference = '';
let month = '';

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
  

  
const handle_otp = function(display_text){
    // change confirm button text to verfiy otp
    $('.modal-form').html(
        "<form  method='POST'>" + 
        '<p class="mb-3 text-center font-size-15">' + display_text + '</p>' +
        '<div id="otp" class="inputs d-flex flex-row justify-content-center mt-2">' +
            '<input class="m-2 text-center form-control rounded otp-inp" type="text" id="first" maxlength="1" />' +
            '<input class="m-2 text-center form-control rounded otp-inp" type="text" id="second" maxlength="1" />' +
            '<input class="m-2 text-center form-control rounded otp-inp" type="text" id="third" maxlength="1" />' +
            '<input class="m-2 text-center form-control rounded otp-inp" type="text" id="fourth" maxlength="1" />' +    
            '<input class="m-2 text-center form-control rounded otp-inp" type="text" id="fifth" maxlength="1" />' +    
            '<input class="m-2 text-center form-control rounded otp-inp" type="text" id="six" maxlength="1" />' +    
        '</div>' +
        '<div class="mb-3 d-flex justify-content-center">' + 
           '<p href="#" id="change_number">No OTP? click <span> <a href="#" class="text-primary fw-bolder"> here </a>  </span> to resend otp number </p>' + 
        '</div>' +
        '<div class="d-flex justify-content-center">' +
        '<button type="button" class="btn btn-light mt-3 mx-2" data-bs-dismiss="modal" aria-label="Close">Cancel</button>'
        + 
        '<button type="button" class="btn btn-danger mt-3 mx-2  verify-otp">Verify OTP</button>' +

        '<div class="spinner-border text-success mx-2 my-n3 d-none" id="otp-payment-loader" role="status">' + 
            '<span class="sr-only">Loading...</span>' + 
        '</div></div></form>'
    )
    OTPInput();
}

const clean_modal = function(){
  $('.modal-form').html(
    `<form  method='POST' class="needs-validation">
    <p class="fw-bolder mb-2" id="modal-amount">Amount :</p>
    <p class="fw-bolder mb-1" id="modal-month">Month: </p>
    <input type='text' class='form-control user_phone_number mb-3' id="payment-phone-number" value="${user_phone}" disabled/>
    <div class="mt-n3 mb-3">
       <a href="#" id="change_number"> Change Momo number</a>
    </div>
    <div>
        <button type="button" class="btn btn-light mt-3 mx-2" data-bs-dismiss="modal" aria-label="Close">Cancel</button>
        <button type="button" class="btn btn-danger mt-3 mx-2  proceed-payment">Proceed to Payment</button>
        <div class="spinner-border text-success mx-2 my-n3 d-none" id='payment-loader' role="status">
            <span class="sr-only">Loading...</span>
        </div>
    </div>
</form>`
  )
}


$(document).on('click', '.pay-dues', function(e){
    dues_id = $(this).data("id")
    amount = $(this).data("amount")
    month = $(this).data("month")
    clean_modal()

    $("#modal-amount").text(`Amount : ${amount} `)
    $("#modal-month").text(`Month : ${month} `)
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
          'amount' : amount,
          'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
          },
      success: function(response){
          $('#payment-loader').addClass('d-none')
          $('.proceed-payment').show()
          console.log(response)
          if (response.status){
              handle_otp(response.data.display_text)
          } else {
              console.log(response.message)
              if (response.message){
                  $('#payment-phone-number').addClass('is-invalid')
                  if ($('#payment-phone-number').next().hasClass('invalid-feedback')){
                      $('.invalid-feedback').remove()
                      $("#payment-phone-number").after(`<p class='invalid-feedback py-n2'> <strong> ${response.message}</strong> </p>`)
                  } else {
                      $("#payment-phone-number").after(`<p class='invalid-feedback py-n2rome'> <strong> ${response.message}</strong> </p>`)
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


$(document).on('click', '.verify-otp', function(e){
  $.ajax({
    type: 'POST',
    url: '/pay-dues/',
    data: {
        'otp' : otp,
        'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
        },
    success: function(response){
      
      console.log(response)
      if (response.status){
        payment_reference = response.data.reference
        $('.modal-form').html(
          `<p class="fw-bolder mb-2 text-center" id="modal-amount">A payment request has been sent to your number. Please complete the payment request on your phone and click done when completed :</p>
                        
          <div class="d-flex justify-content-center align-items-center">
              <button type="button" class="btn btn-light mt-3 mx-2" data-bs-dismiss="modal" aria-label="Close">Cancel</button>
              <button type="button" class="btn btn-danger mt-3 mx-2  proceed-payment">Verify Payment</button>
              <div class="spinner-border text-success mx-2 my-n3 d-none" id='payment-loader' role="status">
                  <span class="sr-only">Loading...</span>
              </div>
          </div>`
        )
      } else {
          console.log(response.message)
          if (response.message){
              $('.otp-inp').addClass('is-invalid')
              if ($('.otp-inp').next().hasClass('invalid-feedback')){
                  $('.invalid-feedback').remove()
                  $(".inputs").after(`<p class='invalid-feedback py-n2'> <strong> ${response.message}</strong> </p>`)
              } else {
                  $(".inputs").after(`<p class='invalid-feedback py-n2rome'> <strong> ${response.message}</strong> </p>`)
              }
              $(".otp-inp").prop('disabled', false)
          }
      }  
    },
    error : function(xhr, errmsg, err){
        console.log(xhr.status + ' ' + xhr.responseText)
    }
        
    })

  $('.verify-payment').on('click', function(){
    $(this).hide()
    $('#otp-payment-loader').removeClass('d-none')
    $.ajax({
      type: 'POST',
      data: {
        reference : payment_reference ,
        dues_id : dues_id 
      },
      success: function(response){
        Swal.fire({
          icon: 'success',
          title: 'Dues paid successfully!',
          text:  `Dues for ${month} paid successfully`,
          confirmButtonColor: "#5664d2"
      }).then(function(){
        location.reload()
      }); 

      }
    })
  })

})



