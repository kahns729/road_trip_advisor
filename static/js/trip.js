var days;

function init(data) {
	days = data;
	show_overview();
	display_description(days[0].events[0]);
}

function show_overview() {
	$("#dropdownMenu1").html("Overview <span class='caret'></span>");
	html_string = "";
	for (var i = 0; i < days.length; i++) {
		html_string += "<h2>Day "+days[i].day.toString()+"</h2><ul class='list-group'>";
		var events = days[i].events;
		for (var j = 0; j < events.length; j++) {
			html_string += "<li class='list-group-item'><button type='button' class='btn btn-default' onclick='display_description("+JSON.stringify(events[j])+")'>"+events[j].name+"</button></li>" 
		}
		html_string += "</ul>"
	}
	$("#events_list").html(html_string);
	setEntireRoute(); // update the map
}

function switch_day(day) {
	$("#dropdownMenu1").html("Day "+ day.toString() + " <span class='caret'></span>");
	for (var i = 0; i < days.length; i++) {
		if (days[i].day == day) {
			display_events(days[i].events);
			setRouteForDay(i); // update the map
		}	
	};
	
}

function display_events(events) {
	var html_string = "";
	for (var i = 0; i < events.length; i++) {
		html_string = html_string+"<li><button type='button' class='btn btn-default' onclick='display_description("+JSON.stringify(events[i])+")'>"+events[i].name+"</button></li>";
	}
	$("#events_list").html(html_string);
}

function display_description(event) {
	var html_string = "";
	if (event.rating_image_url != null) {
		html_string += "<img src=" + event.rating_image_url + " alt='rating' />"
	}
	html_string = html_string + "<h1>" + event.name + "</h1>";
	if (event.subcategory != null && event.subcategory.length > 0) {
		html_string += "<h2>" + event.subcategory[0].localized_name
		if (event.ranking_data != null) {
			html_string += " (" + event.ranking_data.ranking_string + ")"
		}
		html_string += "</h2>"
	}
	if (event.location_string != null) {
		html_string += "<h3>" + event.location_string + "</h3>"
	}
	$("#event_description").html(html_string);
	imageURL = null;
	function makeHttpObject() {
		try {return new XMLHttpRequest();}
		catch (error) {}
		try {return new ActiveXObject("Msxml2.XMLHTTP");}
		catch (error) {}
		try {return new ActiveXObject("Microsoft.XMLHTTP");}
		catch (error) {}

		throw new Error("Could not create HTTP request object.");
	}

	url = "http://api.tripadvisor.com/api/partner/2.0/location/"
	+ event.location_id + "/photos?key=EB205D5CF19247E3BC975276040A7687";

	var request = makeHttpObject();
	request.open("GET", url, true);
	request.send(null);
	request.onreadystatechange = function() {
		console.log("ready state" + request.readyState);
		if (request.readyState == 4) {
			response = JSON.parse(request.responseText);
			data = response["data"];
			if (data != null && data.length > 0) {
				images = data[0]["images"]
				for (var key in images) {
					if (images[key]["url"] != null) {
						console.log(images[key]["url"]);
						imageURL = images[key]["url"];
						html_string += "<img src=" + imageURL + " alt='i'/>";
						$("#event_description").html(html_string);
						return;
					}
				}
			}
		}
	};
}

// function getImage (id) {
// 	imageURL = null;
// 	function makeHttpObject() {
// 		try {return new XMLHttpRequest();}
// 		catch (error) {}
// 		try {return new ActiveXObject("Msxml2.XMLHTTP");}
// 		catch (error) {}
// 		try {return new ActiveXObject("Microsoft.XMLHTTP");}
// 		catch (error) {}

// 		throw new Error("Could not create HTTP request object.");
// 	}

// 	url = "http://api.tripadvisor.com/api/partner/2.0/location/"
// 	+ id + "/photos?key=EB205D5CF19247E3BC975276040A7687";

// 	var request = makeHttpObject();
// 	request.open("GET", url, true);
// 	request.send(null);
// 	request.onreadystatechange = function() {
// 		if (request.readyState == 4) {
// 			response = JSON.parse(request.responseText);
// 			console.log(response);
// 			data = response["data"];
// 			if (data != null && data.length > 0) {
// 				images = data[0]["images"]
// 				for (var key in images) {
// 					if (images[key]["url"] != null) {
// 						console.log(images[key]["url"]);
// 						imageURL = images[key]["url"]
// 						break;
// 					}
// 				}
// 			}
// 		}
// 	};
// }