$(document).on("ready", on_load);
$(document).ajaxStop(on_load_ajax);

if (typeof String.prototype.startsWith != 'function') {
    String.prototype.startsWith = function (str){
        return this.indexOf(str) == 0
    };
}

function on_load () {
    $('.load-in-modal').on('click', load_modal_form)
    $('form:first input[type!=hidden]:first').focus()
}

function on_load_ajax () {
    $('#myModal * form').on('submit', validate_modal_form)
    $('#myModal > form').on('submit', validate_modal_form)
    // $('#myModal input[type!=hidden]:first').focus()
}

function load_modal_form(event) {
    event.preventDefault()

    var url = $(this).attr('href');
    $('#myModal').load(url, function(){
        $(this).modal('show')
    })
}

function validate_modal_form(event) {
    console.log("Enviando form por modal-form")
    event.preventDefault();
    try{
        $($('.modal-dialog button[type=submit]')[0]).html('<i class="icon icon-spinner icon-spin"></i> Cargando...')
            .attr('disabled', true);
            console.log("Spinner!");
    } catch(error){
        console.log(error);
    }


    $.ajax({
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        data: $(this).serialize(),
        success: function(data) {
            if (validateURL(data) || validateURLPath(data)){
                window.location.href = data
            } else if ($(data).find('.modal-body').length) {
                $('#myModal').empty()
                $('#myModal').append(data)
                $('#myModal input[type!=hidden]:first').focus()
            } else {
                location.reload();
            }
        }
    });
}

function validateURL(textval) {
    var urlregex = new RegExp(
        "^(http:\/\/www.|https:\/\/www.|ftp:\/\/www.|www.){1}([0-9A-Za-z]+\.)");
    return urlregex.test(textval);
}

function validateURLPath(textval) {
    var urlregex = new RegExp(
        "^\/.*");
    return urlregex.test(textval);
}
