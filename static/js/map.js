//call json data
var url = "/api/crime.json";
    d3.json(url).then(function(response) {

    console.log(response.crimes);

// Create a map object
var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5
});

// Add a tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 500,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: "pk.eyJ1IjoiYW5hZ3VheW84OSIsImEiOiJja3F1ODNhcmowMXp0MzFsMzh6dm54eTAxIn0.5ipJ_rkH0yV5m7gbdM3Abw"
}).addTo(myMap);

//create function to call locations
//var markers =  L.markerClusterGroup();
    var coordinates = [];
    var vicCount = [];
    
  // Loop through data
for (var i = 0; i < response.length; i++) {

    // Set the data location property to a variable
    var location = response[i]

    // // Check for location property
    // if (location) {

    //   // Add a new marker to the cluster group and bind a pop-up
    //     markers.addLayer(L.marker([location.latitude[1], location.longitude[0]]))
    //     .bindPopup(response[i].State);
    //     console.log(location.latitude[0]);
    
    // };

  // Add our marker cluster layer to the map
myMap.addLayer(markers);
};


console.log("done");
// var stateName = [];
// var murderNumber = [];

// function createMarkers (response) {
//     var state = response.crimes.state
//     console.log(state);
});