$(document).ready(function(){
    let disabled = false
    let email_exists = false
    let phone_number_exists = false


    //Generate user name based on first and other names
    $('#othernames').on('change', function(){
        let othernames = $(this).val()
        let firstname = $('#firstname').val()
        if (firstname){
            $.ajax({
                type: 'POST',
                url: 'generate-username',    
                headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
                data: {
                    first_name:firstname,
                    other_names : othernames
        
                },
        
                success: function(data){
                    $('#username').val(data.username)
                    $('#password').val(data.username)
    
                   
                    
                },
                error : function(xhr, errmsg, err){
                    console.log(xhr.status + ' ' + xhr.responseText)
                }
            });
        }
    });

    //Check if email exists
    $('#email').on('change', function(){
        $.ajax({
            type: 'POST',
            url:"{% url 'check_email' %}",    
            headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
            data: {
                email:$(this).val()
            },
    
            success: function(data){
                console.log(data)
                if(data.exists){
                    $('#email').addClass('is-invalid')
                    $('#feedbackinvalid').css('display', 'block') 
                }
                else {
                    $('#email').addClass('is-valid')
                    $('#email').removeClass('is-invalid')
                    $('#feedbackinvalid').css('display', 'none')
                    email_exists = true
                };
            },   
            error : function(xhr, errmsg, err){
                console.log(xhr.status + ' ' + xhr.responseText)
            }
        });
    });

    //check if phone_number exists
    $('#phone_number').on('change', function(){
        $.ajax({
            type: 'POST',
            url:"{% url 'check_phone_number' %}",    
            headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
            data: {
                phone_number:$(this).val()
            },
            success: function(data){
                console.log(data)
                if(data.exists){
                    $('#phone_number').addClass('is-invalid')
                    $('#phone-invalid').css('display', 'block') 
                    
                }
                else {
                    $('#phone_number').toggleClass('is-valid')
                    $('#phone_number').removeClass('is-invalid')
                    $('#phone-invalid').css('display', 'none') 
                    phone_number_exists = true
                    

                };
            },
               
            error : function(xhr, errmsg, err){
                console.log('Somemethinf')
                console.log(xhr.status + ' ' + xhr.responseText)
            }
        });
    });


    //Remove error bars and messages on input
    $('#phone_number').on('focus', function(){
        $('#phone_number').removeClass('is-valid')
        $('#phone_number').removeClass('is-invalid') 
        $('#phone-invalid').css('display', 'none') 
        $('#email').removeClass('is-valid')
        $('#email').removeClass('is-invalid') 
        $('#feedbackinvalid').css('display', 'none') 

    })


    //Check if all forms are filled and no errors and allow submit
    $(document).on('change keyup', 'input[required]', function(e){
        $("input[required]").each(function() {
          let value = this.value
          if ((value)&&(value.trim() !='') )
              {
                if (phone_number_exists || email_exists) {
                    disabled = true
                }
    
                else {
                    disabled = false
                }
                
              } 
              
            else{
                disabled = true
                return false
              }
        });
    
       if(disabled){
            $('.add_user').prop("disabled", true);
          }else{
            $('.add_user').prop("disabled", false);
          }
     });

})