import config
import urllib, urllib2, math
import json
from geopy.distance import vincenty

def distance(start, end):
	km_to_m = 0.621371
	dist_str = str(vincenty((start["lat"], start["lng"]), (end["lat"], end["lng"])))
	return km_to_m * float(dist_str.split(" ")[0])

def find_waypoints(source, destination):
	url = 'https://maps.googleapis.com/maps/api/directions/json'
	values = {'origin' : source,
	          'destination' : destination,
	          'key' : config.GOOGLEMAPS_API_KEY}
	params = urllib.urlencode(values)
	req = urllib2.Request(url + "?" + str(params))
	response = urllib2.urlopen(req)
	data = json.load(response)
	steps = data["routes"][0]["legs"][0]["steps"]
	# Running count of distance (will be reset every X miles)
	dist_mod = 0
	# Points to query for attractions
	points = []
	count = 0
	for step in steps:
		count += 1
		try:
			step_length = distance(step["start_location"], step["end_location"])
			dist_mod += step_length
		except:
			if count == len(steps):
				points.append({"lng": next_lng, "lat": next_lat})
				break
			else:
				continue
		if step_length > config.DIST_INTERVAL:
			steps.append(step["start_location"])
			# How many segments to split the highway into
			intervals = int(math.ceil(float(step_length) / config.DIST_INTERVAL))
			lng_diff = math.fabs(float(step["start_location"]["lng"]) \
						- float(step["end_location"]["lng"]))
			lat_diff = math.fabs(float(step["start_location"]["lat"]) \
						- float(step["end_location"]["lat"]))
			# Add each division of the highway
			for i in range(intervals):
				next_lng = float(step["start_location"]["lng"]) \
						+ (i+1) * (lng_diff / intervals)
				next_lat = float(step["start_location"]["lat"]) \
						+ (i+1) * (lat_diff / intervals)
				points.append({"lng": next_lng, "lat": next_lat})
		elif dist_mod > config.DIST_INTERVAL:
			points.append(step["start_location"])
			dist_mod = dist_mod % config.DIST_INTERVAL
	duration_str = data["routes"][0]["legs"][0]["duration"]["text"]
	hrs = duration_str.split(" ")[0]
	mins = duration_str.split(" ")[2]
	duration = float(hrs) + float(mins)/60
	return {"points": points, "duration": duration}



print(find_waypoints("USS Alabama, Battleship Parkway, Mobile, AL", "USS Constitution, Boston, MA"))