
    /* data route */
    var url = "/api/crime.json";
    d3.json(url).then(function(response) {

    //console.log(response);
    
    var count = [];
    //var genderCount = {};
    //console.log(response.crimes[0].OffSex);
    var genderArray = response.crimes[0]
    
    var genderCount = d3.nest()
        .key(function(data){
            return data.OffSex

        })
        .entries(response.crimes);
        console.log(genderCount)


    //console.log(genderArray);
    // for (var i = 0; i < genderArray.length; i++) {
    //     count[genderArray[i]] = 1 + (counts[genderArray[i]] || 0).push(genderCount);
    // } 
    

    var data = [{
        values: genderCount,
        labels: ['male', 'female','unknown'],
        type: 'pie'
    }];
    var layout = {
        height: 400,
        width: 500
    };
        Plotly.newPlot("piechart", data, layout);
    });

