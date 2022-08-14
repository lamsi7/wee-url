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
            var full_url = `${response['host']}/${response['gen_id']}`
            var dynamic_el = document.getElementById('gen-id')
            dynamic_el.textContent=full_url
            dynamic_el.href = response['gen_id']


        }
    });
}