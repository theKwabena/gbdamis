$('document').ready(function(){
    let news_id;

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

})