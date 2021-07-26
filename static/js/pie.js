
    /* data route */
    var url = "/api/crime.json";
    d3.json(url).then(function(response) {

    console.log(response);
    
    var count = [];
    //var genderCount = {};
    //console.log(response.crimes[0].OffSex);
    var weaponArray = response.crimes[0].Weapon
    
    var murderWeapon = d3.nest()
        .key(function(data){
            return data.Weapon

        })
        .entries(response.crimes);
        console.log(murderWeapon)
        
        //create lists for murder weapon and values
        var weaponCounts = [];
        var weaponTitles = [];

    for (var i = 0; i < murderWeapon.length; i++) {
        var weaponLabel = murderWeapon[i].key;
        weaponTitles.push(weaponLabel);
        var weaponValues = murderWeapon[i].values.length;
        weaponCounts.push(weaponValues);
        // console.log(weaponLabel);
        // console.log(weaponValues);
        
    }
        console.log(weaponCounts);
        console.log(weaponTitles);


    //console.log(genderArray);
    // for (var i = 0; i < genderArray.length; i++) {
    //     count[genderArray[i]] = 1 + (counts[genderArray[i]] || 0).push(genderCount);
    // } 
    

    var data = [{
        values: weaponCounts,
        labels: weaponTitles,
        automargin: true,
        hole:.4,
        type: 'pie'
    }];
    var layout = {
        height: 600,
        width: 600,
        margin: {"t": 0, "b": 0, "l": 0, "r": 0},
        title:"Weapons Used in Unsolved Murders 2019"
    };
        Plotly.newPlot("piechart", data, layout);
    });

