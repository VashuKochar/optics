$(document).ready(function () {
    $("#run").click(function(){
        console.log("run button clicked");
        run()
    });
});

function fetchmodel() {
    model = {
        atomic_frequency : $("#atomic_frequency").val(),
        atomic_dissipation : $("#atomic_dissipation").val(),
        atomic_initial : $("input[name='atomic_initial']:checked").val(),
        cavity_frequency : $("#cavity_frequency").val(),
        cavity_dissipation : $("#cavity_dissipation").val(),
        cavity_initial : $( "#cavity_initial").val(),
        coupling : $("#coupling").val(),
        thermal : $("#thermal").val(),
        rwa : $("#rwa").val(),
        x : $("#x").val(),
        no_x : $("#no_x").val(),
        t : $("#t").val(),
        no_t : $("#no_t").val(),
    }
    return model
}

function api(resource, data, dom){
    console.log("Fetch request to: " + resource);
    // $.post(resource, data,
    //     function (data, textStatus, jqXHR) {
    //         dom.append(jqXHR);
    //     },
    //     "text"
    // );
    
    $.ajax({
        type: "POST",
        url: resource,
        data: data,
        dataType: "text",
        success: function (response) {
            dom.append(response);
        }
    });
}

function run() {
    model = fetchmodel();
    console.log(model);
    api("rabi",model, $("#rabi"));
    api("wigner",model, $("#wigner"));
}