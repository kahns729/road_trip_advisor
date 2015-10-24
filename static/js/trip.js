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
}

function switch_day(day) {
	$("#dropdownMenu1").html("Day "+ day.toString() + " <span class='caret'></span>");
	for (var i = 0; i < days.length; i++) {
		if (days[i].day == day) {
			display_events(days[i].events);
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
	html_string = html_string + "<h1>" + event.name + "</h1>";
	$("#event_description").html(html_string);
}