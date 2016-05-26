
$('#meeting_form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    send_form();
});
function send_form() {
    console.log("create post is working!") // sanity check
    $.ajax({
        // url : "/send_form/?time=&?n_id=08:001", // the endpoint
        url : window.location.href,
        type : "POST", // http method
        data : {
             the_name : $('#meeting-name').val(),
             the_fullname : $('#meeting-fullname').val(),
             the_email : $('#meeting-email').val()
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            // $('#post-text').val(''); // remove the value from the input
            $('#meeting-name').val('');
            $('#meeting-fullname').val('');
            $('#meeting-email').val('');
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            window.location.assign('http://127.0.0.1:8000/thanks/')
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};