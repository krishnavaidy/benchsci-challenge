$(function() {
    $('#btnGetPmcid').click(function() {
 
        $.ajax({
            url: '/getPmcid',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
