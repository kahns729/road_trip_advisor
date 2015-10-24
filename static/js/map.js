var infowindow = new google.maps.InfoWindow();
var markers = [];

function initMap(itinerary) {

  map = new google.maps.Map(document.getElementById('map'), {
    center: itinerary[0]["start"],
    scrollwheel: false,
    zoom: 7
  });

  var directionsDisplay = new google.maps.DirectionsRenderer({
    map: map
  });

  // Set destination, origin and travel mode.
  var request = {
    destination: itinerary[itinerary.length - 1]["end"],
    origin: itinerary[0]["start"],
    travelMode: google.maps.TravelMode.DRIVING
  };

  // Pass the directions request to the directions service.
  var directionsService = new google.maps.DirectionsService();
  directionsService.route(request, function(response, status) {
    if (status == google.maps.DirectionsStatus.OK) {
      // Display the route on the map.
      directionsDisplay.setDirections(response);
    }
  });

  for (i = 0; i < itinerary.length; i++) {
    markers.push([]);
    day = itinerary[i];
    console.log(day);
    for (j = 0; j < day["events"].length; j++) {
      node = day["events"][j];
      console.log(node);
      createMarker(node["location"]["lat"], node["location"]["lng"], node["name"], i)
    }
  }
}

function createMarker(lat, lng, name, day) {
    //create location
    var loc = new google.maps.LatLng(lat, lng);

    // create new marker
    var mark = new google.maps.Marker({
      map: map,
      position: loc,
      title: name
    });
            
    // Open info window on click of marker
    google.maps.event.addListener(mark, 'click', function() {
      infowindow.close();
      infowindow.setContent(mark.title);
      infowindow.open(map, mark);
    });

    markers[i].push(mark)
}

function showMarkers(day) {
  for (i = 0; i < markers.length; i++) {
    if (i == day) {
      for (marker in markers[i]) {
        marker.setVisible(true);
      }
    }
    else {
      for (marker in markers[i]) {
        marker.setVisible(false);
      }
    }
  }
}