console.log("LOADED")
var submit_btn = document.getElementById("btn-generate-url");
submit_btn.onclick = function(e){
    console.log('here')
    e.preventDefault()

    $.ajax({
        type: "POST",
        url: "generate/",
        data: {
            link:$('#inputURL').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),

        },
        success: function(){
            console.log("successs");
        }
    });
}