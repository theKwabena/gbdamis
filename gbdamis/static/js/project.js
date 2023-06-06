/* Project specific Javascript goes here. */

// $('.modal-title').text('Delete Member')
        // $('.modal-text-content').html('<p class="text-center font-size-15">Are you sure you want to remove' + ' <span class="text-danger fw-bolder fullname"></span> ' + '? Enter <b> password  </b> and click confirm  deletion below to proceed</p>')
        // $('.fullname').text(user_name)
        // $('.confirm-delete').text('Remove Member')
        // $('.confirm-delete').addClass('confirm-remove-member')
        // $("#actions-modal").modal('show') 
   // });

   function OTPInput() {
        const inputs = document.querySelectorAll('#otp > *[id]');
        for (let i = 0; i < inputs.length; i++) {
                inputs[i].addEventListener('keydown', function(event) { 
                        if (event.key==="Backspace" ) {
                                 inputs[i].value='' ; if (i !==0) inputs[i - 1].focus();
                         } else { 
                                if (i===inputs.length - 1 && inputs[i].value !=='' ) { return true; } 
                                else if (event.keyCode> 47 && event.keyCode < 58) { inputs[i].value=event.key; if (i !==inputs.length - 1) inputs[i + 1].focus(); event.preventDefault(); } 
                                else if (event.keyCode> 64 && event.keyCode < 91) { inputs[i].value=String.fromCharCode(event.keyCode);
                                if (i !==inputs.length - 1) inputs[i + 1].focus(); event.preventDefault();
                         } } }); } } OTPInput();


        
            