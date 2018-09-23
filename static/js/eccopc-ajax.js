$(document).ready(function() {
    $('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/wsparcie-techniczne/', {suggestion: query}, function(data){
            $('#sns').html(data);
        });
    });

});