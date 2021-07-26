
    /* data route */
    var url = "/api/crime.json";
    d3.json(url).then(function(response) {

    console.log(response);
    
    var count = [];

    var montharray = response.crimes[0].State
    
    var monthnames = d3.nest()
        .key(function(data){
            return data.Month

        })
        .entries(response.crimes);
        console.log(monthnames)
        
        //create lists for the states and death counts
        var deathCounts = [];
        var monthTitles = [];

    for (var i = 0; i < monthnames.length; i++) {
        var monthLabel = monthnames[i].key;
        monthTitles.push(monthLabel);
        var monthValues = monthnames[i].values.length;
        deathCounts.push(monthValues);
        // console.log(weaponLabel);
        // console.log(weaponValues);
        
    }
        console.log(deathCounts);
        console.log(monthTitles);


    

    var data = [{
        y: deathCounts,
        x: monthTitles,
        type: 'bar'
    }];
    var layout = {
        height: 600,
        width: 800,
        title:"Count of Unsolved Murders by Month in 2019",
        xaxis_title:"State",
        yaxis_title:"Total Murders"
    };
        Plotly.newPlot("barchart", data, layout);
    });

