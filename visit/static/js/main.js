
$('#meeting_form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    send_form();
});
// function send_form() {
//     console.log("create post is working!") // sanity check
//     console.log($('#meeting-hourBegin').val())
//     console.log($('#meeting-hourEnd').val())
//     console.log($('#meeting-day').val())
//     console.log($('#meeting-name').val())
//     console.log($('#meeting-fullname').val())
//     console.log($('#meeting-email').val())
//     console.log($('#meeting-nutritionist').val())
//     // 'hourBegin', 'hourEnd', 'day', 'name', 'fullname', 'email', 'nutritionist'
// };
function send_form() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "/send_form/", // the endpoint
        type : "POST", // http method
        data : {
             the_hourBegin : $('#meeting-hourBegin').val(),
             the_hourEnd : $('#meeting-hourEnd').val(),
             the_day : $('#meeting-day').val(),
             the_name : $('#meeting-name').val(),
             the_fullname : $('#meeting-fullname').val(),
             the_email : $('#meeting-email').val(),
             the_nutritionist : $('#meeting-nutritionist').val()
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            // $('#post-text').val(''); // remove the value from the input
            $('#meeting-hourBegin').val('');
            $('#meeting-hourEnd').val('');
            $('#meeting-day').val('');
            $('#meeting-name').val('');
            $('#meeting-fullname').val('');
            $('#meeting-email').val('');
            $('#meeting-nutritionist').val('');
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