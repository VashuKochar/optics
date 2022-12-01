$(document).ready(function () {
    $("#rabi").click(showRabiGraph);
    $("#wigner").click(function(){
        showWignerGraph();
    });
    $("input.slider").each(function( i ) {
        this.parentElement.previousElementSibling.innerHTML = this.value
        this.oninput = function() {
            console.log("Slider moved");
            console.log(this);
            console.log(this.parentElement);
            // this.before(this.value)
            this.parentElement.previousElementSibling.innerHTML = this.value
            // .prev("p").text();
        }
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

function showRabiGraph() {
    console.log("Show Rabi Graph");
    data = fetchmodel();
    $.ajax({
        type: "POST",
        url: "rabi",
        data: data,
        dataType: "json",
        success:  function (response) {
            console.log(response);
            canvas = $('<canvas id="rabi" width="1000"></canvas>');
            $("#graph").html(canvas);

            new Chart(canvas, {
                type: 'line',
                data: {
                    labels: response.labels,
                    datasets: [{
                        label: 'Cavity',
                        borderColor: 'rgb(255, 0,0)',
                        data: response.data_cavity
                    }, {
                        label: 'Atom excited state',
                        borderColor: 'rgb(0, 0, 255)',
                        data: response.data_atom
                    }]          
                },
                options: {
                    responsive: true,
                        legend: {
                            position: 'top',
                        },
                    title: {
                        display: true,
                        text: 'Vacuum Rabi oscillations'
                    },
                    scales: {
                        xAxes: [{
                          scaleLabel: {
                                display: true,
                                labelString: 'Time'
                            }
                        }],
                        yAxes: [{
                          scaleLabel: {
                                display: true,
                                labelString: 'Occupation probability'
                            }
                        }]
                    }
                }
            });
        },
    });
}
function showWignerGraph() {
    console.log("Show Wigner Graph");
    data = fetchmodel();
    data["tinterest"] = [$("#t1").val(), $("#t2").val(), $("#t3").val(), $("#t4").val()]
    $.ajax({
        type: "POST",
        url: "wigner",
        data: data,
        dataType: "json",
        success:  function (response) {
            console.log(response);
            $("#graphs").empty();
            for (const GraphKey in response.wigner_data) {
                if (Object.hasOwnProperty.call(response.wigner_data, GraphKey)) {
                    const element = response.wigner_data[GraphKey];
                    canvas = $(`<div id="wigner-${GraphKey}"></div>`);
                    $("#graphs").append(canvas);
                    canvas = document.getElementById(`wigner-${GraphKey}`);
                    plotSettings = [ {
                        z: element,
                        x: response.labels,
                        y: response.labels,
                        type: 'contour',
                    }];
                    layout = {
                        autosize: true,
                        width: $( document ).width()/response.wigner_data.length,
                        height: $( document ).width()/response.wigner_data.length,
                        title: `T = ${response.time[GraphKey]}`,
                    }
                    console.log(plotSettings);
                    Plotly.newPlot( canvas, plotSettings, layout);
                }
            }
        },
    });
    console.log(data);
}

// function run() {
//     model = fetchmodel();
//     console.log(model);
//     showRabiGraph(model);
//     showWignerGraph(model);
// }