$(document).ready(function(){
    let csrf = $('#csrf-token').val()
    function IsEmail(email) {
        let regex = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
        return regex.test(email);
      }
    let email_exists = false
    let phone_number_exists = false


    //Generate user name based on first and other names
    $('#othernames').on('change', function(){
        let othernames = $(this).val()
        let firstname = $('#firstname').val()
        if (firstname){
            $.ajax({
                type: 'POST',
                url: '/g-us',    
                headers : {'X-CSRFTOKEN':csrf },
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
    $('#email').on('change keyup', function(){
        if( !IsEmail($(this).val()) ) {
            $('#email').addClass('is-invalid')
            $('#feedbackinvalid').text('This value should be a valid email.')
            $('#feedbackinvalid').css('display', 'block')
        }
        
        else {
            $.ajax({
                type: 'POST',
                url: "/check-email" ,    
                headers : {'X-CSRFTOKEN': csrf},
                data: {
                    email:$(this).val()
                },
        
                success: function(data){
                    console.log(data)
                    if(data.exists){
                        $('#email').addClass('is-invalid')
                        $('#feedbackinvalid').text('This email belongs to another user')
                        $('#feedbackinvalid').css('display', 'block') 
                        email_exists = true
                    }
                    else {
                        $('#email').addClass('is-valid')
                        $('#email').removeClass('is-invalid')
                        $('#feedbackinvalid').css('display', 'none')
                        email_exists = false

                        
                    };
                },   
                error : function(xhr, errmsg, err){
                    console.log(xhr.status + ' ' + xhr.responseText)
                }
            });
        }
        
    });

    //check if phone_number exists
    $('#phone_number').on('change keyup', function(){
        $.ajax({
            type: 'POST',
            url:"/check_phone",    
            headers : {'X-CSRFTOKEN': csrf},
            data: {
                phone_number:$(this).val()
            },
            success: function(data){
                console.log(data)
                if(data.exists){
                    $('#phone_number').addClass('is-invalid')
                    $('#phone-invalid').css('display', 'block')
                    phone_number_exists = true 
                    
                }
                else {
                    $('#phone_number').toggleClass('is-valid')
                    $('#phone_number').removeClass('is-invalid')
                    $('#phone-invalid').css('display', 'none')
                    phone_number_exists = false
                   
                    

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

    })


    $('#email').on('focus', function(){
        $('#email').removeClass('is-valid')
        $('#email').removeClass('is-invalid') 
        $('#feedbackinvalid').css('display', 'none') 

    })


    //Check if all forms are filled and allow submit
    $(document).on('change keyup', 'input[required]', function(e){
    
         $("input[required]").each(function() {
           let value = this.value
           if ((value)&&(value.trim() !=''))
               {
                 disabled = false
               }
            else
            {
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
     
    //On submit check if no errors before proceeding
    $('.add_user').on('click', function(e){
        e.preventDefault();
        if (! $('.add-member-form')[0].checkValidity()) {
            $('.add-member-form')[0].reportValidity()
        }
        else if (phone_number_exists || email_exists){
            
        }
        else {
            $('.user-username').text($('#username').val())
            $('.user-fullname').text($('#firstname').val() + ' ' + $('#othernames').val())
            $('.user-email').text($('#email').val())
            $('.user-phone').text($('#phone_number').val())
            $('.user-password').text($('#username').val())
            $('#myModal').modal('show');
            $('.confirm-add').on('click', function(){
            $('.add-member-form').submit()
            })
        }

    })
    

})