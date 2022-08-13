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
        success: function(response){
            console.log(response)
            console.log("successs");
            // Add new url to the website
            document.getElementById("new-url").className = 'new-url-visible'
            document.getElementById('gen-id').textContent=response['gen_id']


        }
    });
}