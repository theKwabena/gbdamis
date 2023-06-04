$(document).on('click', '#pay-dues', function(e){
    console.log('pay dues clicked')
    $.ajax({
        type: 'GET',
        url: '/pay-dues/',
        data: {
            'name' : 'Name' 
            },
        success: function(data){
            console.log('success')
        },
        error : function(xhr, errmsg, err){
            console.log(xhr.status + ' ' + xhr.responseText)
    }
    
    })
})