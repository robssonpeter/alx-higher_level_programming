$(document).ready(() => {
    $.ajax({
        type: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        CORS: true,
        headers: {
            'Access-Control-Allow-Origin': '*',
        },
        success: (data) => {
            console.log(data)
            //$('DIV#hello').text(data.hello);
        },
        error: (error) => {
            console.log(error)
            alert('hthere is an error');
        }
    });
})