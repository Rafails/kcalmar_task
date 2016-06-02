
$('#meeting_form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });;
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