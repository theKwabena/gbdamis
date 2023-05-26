$(document).ready(function(){
    csrf = $("[name='csrfmiddlewaretoken']")
    let position = $('.position-form').data('value')
    let nomination = $('.nomination-form').data('value');
    let msg = $('.success-message').val()

    const cleanActions = function(){
        $('.actions-modal-title').text('')
        $('.actions-modal-text-content').html('')
        $('.position-name').text('')
        $('.actions-confirm-delete').text('')
        $('.actions-confirm-delete').attr('href', " ")
    };

    const handleApprove = function(approve, decline){
        if (approve){
            
        }
    }

    //If message from a succes function
    if (msg){
        console.log(msg)
        Swal.fire({
            icon: 'success',
            title: msg,
            text:  msg,
            confirmButtonColor: "#5664d2"
        });
    };

    //Empty all modals
    cleanActions();


    const cleanItUp = function(confirmClass){
        $('.modal-confirm').text('')
        $('.modal-confirm').removeClass(confirmClass)
        $('.form-id').val('')
        $('.modal-form')[0].reset()
    };


    //Add Position
    $(document).on('click', '.add-position', function(){
        $('.form-body').html(
            position    
        )
        $('.form-id').val('position-form')
        $('.modal-confirm').text('Add Nomination')
        $('#forms-modal').modal('show')
        if ($('.modal-confirm').hasClass('confirm-add-nomination')){
            $('.modal-confirm').removeClass('confirm-add-nomination ')
        }
        $('.modal-confirm').addClass('confirm-add-position')
    });


    $(document).on('click', '.confirm-add-position', function(e){
        $(this).addClass('hidden')
        e.preventDefault();
        console.log($('.modal-form').serialize())
        $.ajax({
            url: "/nominations/",
            headers : {'X-CSRFTOKEN': csrf },
            method: 'POST',
            data : $('.modal-form').serialize(),
            success : function(response){
                if (response.success){
                    $('#forms-modal').modal('hide')
                    cleanItUp('confirm-add-position')
                    Swal.fire({
                        icon: 'success',
                        title: response.title,
                        text:  response.text,
                        confirmButtonColor: "#5664d2"
                    }).then(function(){
                        location.reload()
                    });

                } else {
                    data = JSON.parse(response.errors)
                    console.log(data)
                    if (data.name){
                        $('#id_name').addClass('is-invalid')
                        if ($('#id_name').next().hasClass('invalid-feedback')){
                            $('.invalid-feedback').remove()
                            $("#id_name").after("<p class='invalid-feedback'> <strong>"  + data.name[0].message + "</strong> </p>")
                        } else {
                            $("#id_name").after("<p class='invalid-feedback'> <strong>"  + data.name[0].message + "</strong> </p>")
                        }
                    }

                }
            },

            error : function(xhr, errmsg, err){
                    console.log(xhr.status + ' ' + xhr.responseText)
            }
        });
    });


    //Add Nomination
    $(document).on('click', '.add-nomination', function(){
        console.log('clicked')
        $('.form-body').html(
            nomination
        )
        $('.form-id').val('nomination-form')
        $('.modal-confirm').text('Add Nomination')
        $('#forms-modal').modal('show')
        if ($('.modal-confirm').hasClass('confirm-add-position')){
            $('.modal-confirm').removeClass('confirm-add-position')
        }
        $('.modal-confirm').addClass('confirm-add-nomination')
    });


    //Confirm add nomination
    $(document).on('click', '.confirm-add-nomination', function(e){
        $(this).attr('disabled', 'disabled')
        e.preventDefault();
        console.log($('.modal-form').serialize())
        $.ajax({
            url: "/nominations/",
            headers : {'X-CSRFTOKEN': csrf },
            method: 'POST',
            data : $('.modal-form').serialize(),
            success : function(response){
                if (response.success){
                    $('#forms-modal').modal('hide')
                    cleanItUp('confirm-add-position')
                    Swal.fire({
                        icon: 'success',
                        title: response.title,
                        text:  response.text,
                        confirmButtonColor: "#5664d2"
                    }).then(function(){
                        location.reload()
                    });

                } else {
                    data = JSON.parse(response.errors)
                    console.log(data)
                    if (data.nominee){
                        $('#id_nominee').addClass('is-invalid')
                        if ($('#id_nominee').next().hasClass('invalid-feedback')){
                            $('.modal-confirm').removeClass('confirm-add-nomination ')
                            $("#id_nominee").after("<p class='invalid-feedback'> <strong>"  + data.nominee[0].message + "</strong> </p>")
                        } else {
                            $("#id_nominee").after("<p class='invalid-feedback'> <strong>"  + data.nominee[0].message + "</strong> </p>")
                        }
                    }
                    if (data.position){
                        $('#id_position').addClass('is-invalid')
                        if ($('#id_position').next().hasClass('invalid-feedback')){
                            $('')
                        } else {
                            $("#id_position").after("<p class='invalid-feedback'> <strong>"  + data.position[0].message + "</strong> </p>")
                        }
                    }

                }
            },

            error : function(xhr, errmsg, err){
                    console.log(xhr.status + ' ' + xhr.responseText)
            }
        });
    });
    

    //Delete Position
    $(document).on('click', '.delete-position', function(){
        position = $(this).data('position')
        position_id = $(this).data('id')
        $('.actions-modal-title').text('Remove Position')
        $('.actions-modal-text-content').html('<p class="text-center font-size-15">Are you sure you want to remove the position' + ' <span class="text-danger fw-bolder position-name"></span> ' + 'from avialable positions? All nominations for this position will be <b> deleted  </b>. Click confirm  deletion below to proceed</p>')
        $('.position-name').text(position)
        $('.actions-confirm-delete').data('position_id', position_id) 
        $('.actions-confirm-delete').text('Remove Position')
        // $('.actions-confirm-delete').attr('href', "/position/" + position_id + "/")
        $("#actions-modal").modal('show') 
    })

    $(document).on('click', '.actions-confirm-delete', function(){
        position_id = $(this).data('position_id')
        console.log('clicked')
        $(this).hide()
        $(this).after(
           "<div class='spinner-border text-success mt-3'>"
           +"<span class='sr-only'>Loading...</span></div>"
        )
        location.href= "/position/" + position_id
    })

    $(document).on('click', '.delete-nomination', function(){
        nomination = $(this).data('nomination')
        $('.actions-modal-title').text('Remove Nominee')
        $('.actions-modal-text-content').html('<p class="text-center font-size-15">Are you sure you want to remove this nominee' + ' <span class="text-danger fw-bolder position-name"></span> ' + 'from avialable positions? All nominations for this position will be <b> deleted  </b>. Click confirm  deletion below to proceed</p>')
        // $('.position-name').text(nomination)
        $('.actions-confirm-delete').text('Remove Nomination')
        // $('.actions-confirm-delete').attr('href', "/nomination/" + nomination + "/")
        $("#actions-modal").modal('show') 

    })

   
    
    //Clear errors on form select
    $(document).on('focus', '.form-select', function(){
        if ($(".modal-confirm").is(":disabled")){
            $('.modal-confirm').removeAttr("disabled");  
        }
        $('#id_nominee').removeClass('is-invalid') 
        $('#id_position').removeClass('is-invalid') 
        $('.invalid-feedback').remove() 
    });

    $(document).on('keyup', '.textinput', function(){
        if ($(".modal-confirm").is(":disabled")){
            $('.modal-confirm').removeAttr("disabled");  
            $(this).removeClass('is-invalid') 
            $('.invalid-feedback').remove() 

        }
    })




});