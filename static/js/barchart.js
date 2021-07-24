
    /* data route */
    var url = "/api/crime.json";
    d3.json(url).then(function(response) {

    console.log(response);
    
    var count = [];

    var statearray = response.crimes[0].State
    
    var statenames = d3.nest()
        .key(function(data){
            return data.State

        })
        .entries(response.crimes);
        console.log(statenames)
        
        //create lists for the states and death counts
        var deathCounts = [];
        var stateTitles = [];

    for (var i = 0; i < statenames.length; i++) {
        var stateLabel = statenames[i].key;
        stateTitles.push(stateLabel);
        var stateValues = statenames[i].values.length;
        deathCounts.push(stateValues);
        // console.log(weaponLabel);
        // console.log(weaponValues);
        
    }
        console.log(deathCounts);
        console.log(stateTitles);


    

    var data = [{
        y: deathCounts,
        x: stateTitles,
        type: 'bar'
    }];
    var layout = {
        height: 600,
        width: 600,
        title:"Unsolved Murders by State in 2019",
        xaxis_title:"State",
        yaxis_title:"Total Murders"
    };
        Plotly.newPlot("barchart", data, layout);
    });

