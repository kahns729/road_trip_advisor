var infowindow = new google.maps.InfoWindow();
var markers = [];
var itinerary = {};
var initialized = false;

function initMap(itin) {
  itinerary = itin;

  map = new google.maps.Map(document.getElementById('map'), {
    center: createLocation(itinerary[0]["start"]),
    scrollwheel: false,
    zoom: 10
    //mapTypeId: google.maps.MapTypeId.TERRAIN
  });

  directionsDisplay = new google.maps.DirectionsRenderer({
    map: map
  });

  initialized = true;
  setEntireRoute();

  // for (i = 0; i < itinerary.length; i++) {
  //   markers.push([]);
  //   day = itinerary[i];
  //   for (j = 0; j < day["events"].length; j++) {
  //     node = day["events"][j];
  //     createMarker(createLocation(node["location"]), node["name"], i);
  //   }
  // }
}

function setEntireRoute() {
  if (!initialized) {
    return
  }

  directionsDisplay.setDirections({routes: []});

  // Set destination, origin and travel mode.
  var request = {
    destination: createLocation(itinerary[itinerary.length - 1]["end"]),
    origin: createLocation(itinerary[0]["start"]),
    waypoints: getWaypoints(),
    optimizeWaypoints: true,
    travelMode: google.maps.TravelMode.DRIVING
  };

  // Pass the directions request to the directions service.
  var directionsService = new google.maps.DirectionsService();
  directionsService.route(request, function(response, status) {
    if (status == google.maps.DirectionsStatus.OK) {
      console.log("directionsServer request success");
      // Display the route on the map.
      directionsDisplay.setDirections(response);
    } else {
      console.log(response);
    }
  });
}

function setRouteForDay(d) {
  directionsDisplay.setDirections({routes: []});

  var waypoints = []
  day = itinerary[d]
  for (j = 0; j < day["events"].length; j++) {
    node = day["events"][j];
    waypoints.push(createWaypoint(node["location"]));
  }

  // Set destination, origin and travel mode.
  var request = {
    destination: createLocation(day["end"]),
    origin: createLocation(day["start"]),
    waypoints: waypoints,
    optimizeWaypoints: true,
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
}

function createLocation(locPair) {
  console.log(JSON.stringify(locPair));
  return new google.maps.LatLng(parseFloat(locPair["lat"]), parseFloat(locPair["lng"]));
}

function getWaypoints() {
  locations = []
  for (i = 0; i < itinerary.length; i++) {
    day = itinerary[i];
    if (i != 0) {
      locations.push(createWaypoint(day["start"]));
    }
    for (j = 0; j < day["events"].length; j++) {
      node = day["events"][j];
      if (node["category"]["name"] == "hotel") {
        locations.push(createWaypoint(node["location"]));
      }
    }
  }
  return locations;
}

function createWaypoint (loc) {
  return {
    location: createLocation(loc),
    stopover: true
  }
}

function createMarker(loc, name, day) {
  // create new marker
  var mark = new google.maps.Marker({
    map: map,
    position: createLocation(loc),
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