let msg = $('.success-message').val()
if (msg){
    console.log(msg)
    Swal.fire({
        icon: 'success',
        title: msg,
        text:  msg,
        confirmButtonColor: "#5664d2"
    });
};

$(document).ready(function(){
    csrf = $("[name='csrfmiddlewaretoken']")
    let position = $('.position-form').data('value')
    let nomination = $('.nomination-form').data('value');
    

    const cleanActions = function(){
        $('.actions-modal-title').text('')
        $('.actions-modal-text-content').html('')
        if($('.actions-confirm-button').attr('data-position_id')){
            $('.actions-confirm-button').removeAttr('data-position_id')
        }
        if($('.actions-confirm-button').attr('data-nominee')){
            $('.actions-confirm-button').removeAttr('data-nominee_id')
        }


        if ($('.actions-confirm-button').hasClass('confirm-delete-position')){
            $('.modal-confirm').removeClass('confirm-delete-position ')
        }
        if ($('.modal-confirm').hasClass('confirm-delete-nomination')){
            $('.modal-confirm').removeClass('confirm-add-nomination ')
        }
        $('.actions-confirm-button').text('')
    };

    const showFormModal = function(title, form_name, form_id, confirm_button, new_class){
        cleanForms()
        $('.forms-modal-title').text(title)
        $('.form-body').html(
            form_name
        )
        $('.form-id').val(form_id)
        $('.forms-modal-confirm').text(confirm_button)
        $('#forms-modal').modal('show')
        $('.forms-modal-confirm').addClass(new_class)
    }

    const cleanForms = function(){
        $('.forms-modal-title').text('')
        $('.form-body').html('')
        $('.form-id').val('')
        $('.forms-modal-confirm').text('')
        if ($('.forms-modal-confirm').hasClass('confirm-add-nomination')){
            $('.modal-confirm').removeClass('confirm-add-nomination ')
        }
        if ($('.modal-confirm').hasClass('confirm-add-position')){
            $('.modal-confirm').removeClass('confirm-add-position ')
        }
    };


    const handleApprove = function(title, action, nominee_name, position, nominee_id, button_name){
        cleanActions()
        $('.actions-modal-title').text(title)
        $('.actions-modal-text-content').html(
            '<div class="text-center">' + 
            '<p class="text-center font-size-15">Are you sure you want to '
            + action  + ' this nomination? </p>' + 
            '<p class="text-danger fw-bolder nominee-name"></p> ' + 
            '<p> Click ' + action +  ' nomination below to proceed</p>' + '</div>'
        )
        $('.nominee-name').text(`${nominee_name} |  ${position}`)
        $('.actions-confirm-button').attr('data-nominee_id', nominee_id)
        $('.actions-confirm-button').addClass(`confirm-${action}-nomination`)
        $('.actions-confirm-button').text(button_name)
        $('#actions-modal').modal('show')
    }


   


 


    //Add Position
    $(document).on('click', '.add-position', function(){
        cleanForms()
        showFormModal(
            'Add New Position',
            position,
            'position-form',
            'Add Position',
            'confirm-add-position',
        )

        // $('.forms-modal-title').text('Add New Position')
        // $('.form-body').html(
        //     position    
        // )
        // $('.form-id').val('position-form')
        // $('.forms-modal-confirm').text('Add Positon')
        // $('.forms-modal-confirm').addClass('confirm-add-position')
        // $('#forms-modal').modal('show')
    });


    $(document).on('click', '.confirm-add-position', function(e){
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
        showFormModal(
            'Add New Nominee',
            nomination, 
            'nomination-form',
            'Add Nomination',
            'confirm-add-nomination'
        );
        // $('.form-body').html(
        //     nomination
        // )
        // $('.form-id').val('nomination-form')
        // $('.modal-confirm').text('Add Nomination')
        // $('#forms-modal').modal('show')
        // if ($('.modal-confirm').hasClass('confirm-add-position')){
        //     $('.modal-confirm').removeClass('confirm-add-position')
        // }
        // $('.modal-confirm').addClass('confirm-add-nomination')
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
        cleanActions()
        let position_name = $(this).data('position')
        let position_id = $(this).data('id')
        $('.actions-modal-title').text('Remove Position')
        $('.actions-modal-text-content').html('<p class="text-center font-size-15">Are you sure you want to remove the position' + ' <span class="text-danger fw-bolder position-name"></span> ' + 'from avialable positions? All nominations for this position will be <b> deleted  </b>. Click confirm  deletion below to proceed</p>')
        $('.position-name').text(position_name)
        $('.actions-confirm-button').attr('data-position_id', position_id) 
        $('.actions-confirm-button').addClass('confirm-delete-position')
        $('.actions-confirm-button').text('Remove Position')
        $("#actions-modal").modal('show') 
        console.log(position_id )
    })

    
    $(document).on('click', '.confirm-delete-position', function(){
        let position_id = $(this).data('position_id')
        console.log(position_id)
        $(this).hide()
        $(this).after(
           "<div class='spinner-border text-success mt-3'>"
           +"<span class='sr-only'>Loading...</span></div>"
        )
        location.href= "/position/" + position_id
    })

    $(document).on('click', '.delete-nomination', function(){
        cleanActions()
        let nominee_id = $(this).data('nominee_id')
        let nominee_name = $(this).data('nominee_name')
        $('.actions-modal-title').text('Remove Nominee')
        $('.actions-modal-text-content').html('<p class="text-center font-size-15">Are you sure you want to remove' + ' <span class="text-danger fw-bolder nominee-name"></span> ' + 'from the list of <b> nominees  </b>. Click remove nominee below to proceed</p>')
        $('.nominee-name').text(nominee_name)
        $('.actions-confirm-button').attr('data-nominee_id', nominee_id)
        $('.actions-confirm-button').addClass('confirm-delete-nomination')
        $('.actions-confirm-button').text('Remove Nomination')
        // $('.actions-confirm-delete').attr('href', "/nomination/" + nomination + "/")
        $("#actions-modal").modal('show') 

    })

    


    $(document).on('click', '.confirm-delete-nomination', function(){
        let nomination_id = $(this).data('nominee_id')
        console.log(nomination_id)
        $(this).hide()
        $(this).after(
           "<div class='spinner-border text-success mt-3'>"
           +"<span class='sr-only'>Loading...</span></div>"
        )
        location.href= "/nomination/" + nomination_id + '/delete'
    })


    $(document).on('click', '.approve-nomination', function(){
        console.log('clicked')
        let nominee_id = $(this).data('nominee_id')
        let nominee_name = $(this).data('nominee_name')
        let position = $(this).data('nominee_position')
        handleApprove(
            'Approve Nomination',
            'approve',
            nominee_name,
            position,
            nominee_id,
            'Approve Nomination'
        )
    })




    $(document).on('click', '.confirm-approve-nomination', function(){
        let nomination_id = $(this).data('nominee_id')
        console.log(nomination_id)
        $(this).hide()
        $(this).after(
           "<div class='spinner-border text-success mt-3'>"
           +"<span class='sr-only'>Loading...</span></div>"
        )
        location.href= "/nominations/" + nomination_id + '/approve'
    })

    $(document).on('click', '.decline-nomination', function(){
        console.log('clicked')
        let nominee_id = $(this).data('nominee_id')
        let nominee_name = $(this).data('nominee_name')
        let position = $(this).data('nominee_position')
        handleApprove(
            'Decline Nomination',
            'decline',
            nominee_name,
            position,
            nominee_id,
            'Decloine Nomination'
        )
    })
   
    $(document).on('click', '.confirm-decline-nomination', function(){
        let nomination_id = $(this).data('nominee_id')
        console.log(nomination_id)
        $(this).hide()
        $(this).after(
           "<div class='spinner-border text-success mt-3'>"
           +"<span class='sr-only'>Loading...</span></div>"
        )
        location.href= "/nominations/" + nomination_id + '/decline'
    })
    
    //Clear errors on form select
    $(document).on('focus', '.form-select', function(){
        if ($(".forms-modal-confirm").is(":disabled")){
            $('.forms-modal-confirm').removeAttr("disabled");  
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