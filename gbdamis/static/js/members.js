$('document').ready(function(){
    //Global Variables ID
    let member_id; 
    //Confirm Password 

    //If page contains a message 
    let msg = $('.success-message').val()
        if (msg){
            console.log(msg)
            Swal.fire({
                icon: 'success',
                title: 'User added successfully!',
                text:  msg,
                confirmButtonColor: "#5664d2"
            });
        } 
    
    //Clear all errors on user input
    function confirm_password(onSuccess, onError){
        if (!$('#user_password').val()){                
            $('#user_password').addClass('is-invalid')
            console.log('Here it is')
        }
        else {
            console.log('Starting call')
            $.ajax({
                url: "/check-password",
                headers : {'X-CSRFTOKEN': csrfToken },
                method: 'POST',
                data : {
                    password : $('#user_password').val()
                },
                success : function(response){
                    if (response.has_permission){
                        console.log('Success')
                        onSuccess();
                    }

                    else {
                        console.log('No perm')
                        onError();
                    }
                },

                error : function(xhr, errmsg, err){
                        console.log(xhr.status + ' ' + xhr.responseText)
                }
            });
        }
    }

    const handleActions = function(title, content, text, buttonName, newClassName ){
        $('.modal-title').text(title)
        $('.modal-text-content').html(content)
        $('.fullname').text(text)
        $('.confirm-delete').text(buttonName)
        $('.confirm-delete').addClass(newClassName)
        $('#user_password').val('')
        $("#actions-modal").modal('show')
        return true;
    }

    const cleanItUp = function(class_name){
        $('#user_password').val('')
            $('.confirm-password').removeClass(class_name)
            $('#actions-modal').modal('hide')
        
    }

    //Remove User
    $('.remove-member').on('click', function(event){
        console.log('clicked')
        member_id = $(this).data('value')
        user_name = $(this).data('fullname')
        handleActions(
            title = 'Delete Member',
            content ='<p class="text-center font-size-15">Are you sure you want to remove' 
            +' <span class="text-danger fw-bolder fullname"></span> ' 
            + '? Enter <b> password  </b> and click confirm  deletion below to proceed</p>',
            text = user_name,
            buttonName = 'Remove Member',
            newClassName = 'confirm-remove-member'
        ) 
    });
    //Confirm remove User
    $(document).on('click', '.confirm-remove-member', function(event){
        event.preventDefault()
        console.log('CLicked remove')
        confirm_password(
            //On success
            function(){
                console.log('check success')
                let url = 'remove-member/' + member_id
                $.ajax({
                    url: url,
                    headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
                    method: 'GET',
                    success : function(response){
                        cleanItUp('confirm-remove-member')
                        if (response.deleted){
                        Swal.fire({
                            icon: 'success',
                            title: 'User removed successfull!',
                            text: 'User has been successfully removed from the system',
                            confirmButtonColor: "#5664d2"
                
                        }).then(function(){
                            location.reload();
                        });
                        
                        
                        
                        }
                        else {
                            console.log('An error occured')
                        }
                        
                    },
                    error : function(xhr, errmsg, err){
                            console.log(xhr.status + ' ' + xhr.responseText)
                            
                    }
                    
                });
            },

            //On Error
            function(){
                console.log('Sorry no perm')
                $('#user_password').addClass('is-invalid')
                $('#feedbackinvalid').css('display', 'block') 
            }

        )
    });


    //Make Admin
    $('.make-admin').on('click', function(event){
        console.log('clicked')
        member_id = $(this).data('value')
        user_name = $(this).data('fullname')
        handleActions(
            title = 'Make Admin',
            content ='<p class="text-center font-size-15">Are you sure you want to make' 
            +' <span class="text-danger fw-bolder fullname"></span> ' 
            + 'an admin? Enter <b> password  </b> and click confirm below to proceed</p>',
            text = user_name,
            buttonName = 'Make Admin',
            newClassName = 'confirm-make-admin'
        ) 
    });

    $(document).on('click', '.confirm-make-admin', function(event){
        event.preventDefault()
        console.log('CLicked remove')
        confirm_password(
            //On success
            function(){
                console.log('check success')
                let url = 'member/' + member_id +'/make-admin'
                $.ajax({
                    url: url,
                    method: 'GET',
                    success : function(response){
                        console.log(response)
                        if(response.success){ 
                            cleanItUp('confirm-make-admin')
                            Swal.fire({
                                icon: 'success',
                                title: 'User is now an admin!',
                                text: 'User has been made an admin successfully',
                                confirmButtonColor: "#5664d2"
                    
                            }).then(function(){
                                location.reload()
                            });
                            

                        }
                        else {
                            console.log('An error occured')
                        }
                        
                    },
                    error : function(xhr, errmsg, err){
                            console.log(xhr.status + ' ' + xhr.responseText)
                            
                    }
                    
                });
            },

            //On Error
            function(){
                console.log('Sorry no perm')
                $('#user_password').addClass('is-invalid')
                $('#feedbackinvalid').css('display', 'block') 
            }

        )
    });

    $('.remove-admin').on('click', function(){
        member_id = $(this).data('value')
        user_name = $(this).data('fullname')
        handleActions(
            title = 'Remove as Admin',
            content ='<p class="text-center font-size-15">Are you sure you want to remove' 
            +' <span class="text-danger fw-bolder fullname"></span> ' 
            + 'as an admin? Enter <b> password  </b> and click confirm below to proceed</p>',
            text = user_name,
            buttonName = 'Remove as Admin',
            newClassName = 'confirm-remove-admin'
        ) 
    });

    $(document).on('click', '.confirm-remove-admin', function(event){
        event.preventDefault()
        confirm_password(
            function(){
                let url = 'member/' + member_id +'/remove-admin'
                $.ajax({
                    url: url,
                    headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
                    method: 'GET',
                    success : function(response){
                        console.log(response)
                        if(response.success){ 
                            cleanItUp('confirm-remove-modal')
                            Swal.fire({
                                icon: 'success',
                                title: 'User removed as an admin!',
                                text: 'User removed from admin memebers successfully',
                                confirmButtonColor: "#5664d2"
                    
                            }).then(function(){
                                location.reload();
                            });
                        }                        
                        
                        
                        
                        
                    },
                    error : function(xhr, errmsg, err){
                            console.log(xhr.status + ' ' + xhr.responseText)
                            
                    }
                    
                });
            },
            function(){
                console.log('Sorry no perm')
                $('#user-password').addClass('is-invalid')
                $('#feedbackinvalid').css('display', 'block') 
            }

        )
            
        
    });
   



});


    //Confirm Delete User
//     $('.confirm-delete').on('click', function(event){
//         event.preventDefault()
//         if (!$('#password').val()){                
//             $('#password').addClass('is-invalid')
//         }
//         else {
//             let url = 'remove-member/' + member_id
//             $.ajax({
//                 url: "{% url 'check_password' %}",
//                 headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
//                 method: 'POST',
//                 data : {
//                     password : $('#password').val()
//                 },
//                 success : function(response){
//                     let url = 'remove-member/' + member_id
//                     $.ajax({
//                         url: url,
//                         headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
//                         method: 'POST',
//                         success : function(response){
//                             $("#row-" + member_id).remove()
                            
//                             Swal.fire({
//                                 icon: 'success',
//                                 title: 'User removed successfull!',
//                                 text: 'User has been successfully removed from the system',
//                                 confirmButtonColor: "#5664d2"
                    
//                             });
//                             $('#password').val('')
//                             $('#delete-modal').modal('hide')
                            
//                         },
//                         data : {
//                             password : $('.user_password').val()
//                         },
//                         error : function(xhr, errmsg, err){
//                                 console.log(xhr.status + ' ' + xhr.responseText)
                                
//                         }
                        
//                     });
//                 },
                
//                 error : function(xhr, errmsg, err){
//                         console.log(xhr.status + ' ' + xhr.responseText)
//                         $('#' + id + 'password').addClass('is-invalid')
//                         $('#feedbackinvalid').css('display', 'block') 

                        
//                 }
                
//             });
//         }
//     });


//     //Make Admin
//     $('.make-admin').on('click', function(event){
//         member_id = $(this).data('value')
//         name = $(this).data('fullname')
//         $('.admin-fullname').text(name)
//         $("#make-admin-modal").modal('show') 
//     });

//     //Confirm Make Admin
//     $('.confirm-admin').on('click', function(event){
//         event.preventDefault()
//         if (!$('#admin-password').val()){                
//             $('#admin-password').addClass('is-invalid')
//         }
//         else {
//             $.ajax({
//                 url: "{% url 'check_password' %}",
//                 headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
//                 method: 'POST',
//                 data : {
//                     password : $('#admin-password').val()
//                 },
//                 success : function(response){
//                     let url = 'member/' + member_id + '/make-admin'
//                     $.ajax({
//                         url: url,
//                         headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
//                         method: 'GET',
//                         success : function(response){
//                             console.log(response)
//                             if(response.success){
//                                 $("#make-admin-modal").modal('hide') 

//                                 Swal.fire({
//                                     icon: 'success',
//                                     title: 'User is now an admin!',
//                                     text: 'User has been made an admin successfully',
//                                     confirmButtonColor: "#5664d2"
                        
//                                 });
//                             }
                            
//                             $('#admin-password').val('')
//                             $('#delete-modal').modal('hide')
                            
//                         },
//                         data : {
//                             password : $('#admin-password').val()
//                         },
//                         error : function(xhr, errmsg, err){
//                                 console.log(xhr.status + ' ' + xhr.responseText)
                                
//                         }
                        
//                     });
//                 },
                
//                 error : function(xhr, errmsg, err){
//                         console.log(xhr.status + ' ' + xhr.responseText)
//                         $('#admin-password').addClass('is-invalid')
//                         $('#feedbackinvalid').css('display', 'block') 

                        
//                 }
                
//             });
//         }
//     });


//     //Remove as Admin
//     $('.remove-admin').on('click', function(event){
//         member_id = $(this).data('value')
//         name = $(this).data('fullname')
//         $('.modal-title').text('Remove as Admin')
//         $('.modal-text-content').html('<p class="text-center font-size-15">Are you sure you want to remove' + ' <span class="text-danger fw-bolder admin-fullname"></span> ' + 'an admin? Enter <b> password  </b> and click confirm  deletion below to proceed</p>')
//         $('.admin-fullname').text(name)
//         $('.confirm-password').text('Remove as Admin')
//         $('.confirm-password').addClass('confirm-remove-admin')
//         $("#make-admin-modal").modal('show') 
//     });


//     $(document).on('click', '.confirm-remove-admin', function(event){
//         event.preventDefault()
//         confirm_password(
//             function(){
//                 let url = 'member/' + member_id +'/remove-admin'
//                 $.ajax({
//                     url: url,
//                     headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
//                     method: 'GET',
//                     success : function(response){
//                         console.log(response)
//                         if(response.success){
//                             $("#make-admin-modal").modal('hide') 

//                             Swal.fire({
//                                 icon: 'success',
//                                 title: 'User is now an admin!',
//                                 text: 'User has been made an admin successfully',
//                                 confirmButtonColor: "#5664d2"
                    
//                             });
//                         }
                        
//                         $('#admin-password').val('')
//                         $('#delete-modal').modal('hide')
//                         $('.b-'+member_id).remove()
//                         $('.confirm-remove-admin').val('')
//                         $('.confirm-password').removeClass('confirm-remove-admin')
                        
//                     },
//                     error : function(xhr, errmsg, err){
//                             console.log(xhr.status + ' ' + xhr.responseText)
                            
//                     }
                    
//                 });
//             },
//             function(){
//                 console.log('Sorry no perm')
//                 $('#user-password').addClass('is-invalid')
//                 $('#feedbackinvalid').css('display', 'block') 
//             }

//         )
            
        
//     });


//     function confirm_password(onSuccess, onError){
//         if (!$('#user-password').val()){                
//             $('#user-password').addClass('is-invalid')
//             console.log('Here it is')
//         }
//         else {
//             console.log('Starting call')
//             $.ajax({
//                 url: "{% url 'check_password' %}",
//                 headers : {'X-CSRFTOKEN': '{{ csrf_token }}' },
//                 method: 'POST',
//                 data : {
//                     password : $('#user-password').val()
//                 },
//                 success : function(response){
//                     if (response.has_permission){
//                         console.log('Success')
//                         onSuccess();
//                     }

//                     else {
//                         console.log('No perm')
//                         onError();
//                     }
//                 },

//                 error : function(xhr, errmsg, err){
//                         console.log(xhr.status + ' ' + xhr.responseText)
//                 }
//             });
//         }
//     }


// });