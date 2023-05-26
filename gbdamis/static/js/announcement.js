    $(document).ready(function(){
        let msg = $('.success-message').val()
        if (msg){
            console.log(msg)
            Swal.fire({
                icon: 'success',
                title: msg,
                text:  msg,
                confirmButtonColor: "#5664d2"
            });
        }  
        
        
        $('.confirm-edit-news').on('click', function(e){
            e.preventDefault()
            news_id = $(this).data('value')
            data = get_item(news_id)
            console.log(data)
            console.log($('#new-description').val())
            console.log(news_id)
            $.ajax({
                type: 'POST',
                url: "{% url 'news' %}" ,    
                headers :{'X-CSRFTOKEN': '{{ csrf_token }}' },
                data: {
                   action: 'update',
                   news_id : news_id,
                   new_title : $('#new-title').val(),
                   new_description : $('#new-description').val()
    
                },
        
                success: function(data){
                    $('#new-'+news_id).text($('#new-title').val())
                    $('#description-'+news_id).text($('#new-description').val())
                    $('#edit-news').modal('hide')
                    if(data.message){
                        Swal.fire({
                            icon: 'success',
                            title: data.message,
                            text:  data.message,
                            confirmButtonColor: "#5664d2"
                        });
                    }
                    console.log('success')
                },   
                error : function(xhr, errmsg, err){
                    console.log(xhr.status + ' ' + xhr.responseText)
                }
            });
        });
    
    });

   

  
    $(document).on('click', '.delete-news', function(e){
        e.preventDefault()
        news_id = $(this).attr('id')
        console.log(news_id)
        console.log($('#new-description').val())
        console.log(news_id)
        $.ajax({
            type: 'POST',
            url: "{% url 'news' %}" ,    
            headers :{'X-CSRFTOKEN': '{{ csrf_token }}' },
            data: {
               action: 'delete',
               news_id : news_id,
            },
    
            success: function(data){
                $("#row-" + news_id).remove()
                $('#delete-news').modal('hide')
                if(data.message){
                    Swal.fire({
                        icon: 'success',
                        title: data.message,
                        text:  data.message,
                        confirmButtonColor: "#5664d2"
                    });
                }
                console.log('success')
            },   
            error : function(xhr, errmsg, err){
                console.log(xhr.status + ' ' + xhr.responseText)
            }
        });
    });