import urllib2, json, config

def getJSON (lat, lon, extra = None):
	address = "http://api.tripadvisor.com/api/partner/2.0/map/"
	address += str(lat) + "," + str(lon)
	if extra:
		address += "/" + extra
	address += "?key=" + config.TRIPADVISOR_API_KEY
	address += "&distance=" + str(config.LOCATION_RADIUS)
	JSON = json.loads(urllib2.urlopen(address).read())
	return JSON['data']

# needed for conversion to google maps
def parseJSON (json):
	json["location"] = {"lat" : float(json["latitude"]), "lng" : float(json["longitude"])}
	return json

def getFood (lat, lon):
	return [parseJSON(json) for json in getJSON(lat, lon, "restaurants")]
	# return getJSON(lat, lon, "restaurants")

def getHotels (lat, lon):
	return [parseJSON(json) for json in getJSON(lat, lon, "hotels")]
	# return getJSON(lat, lon, "hotels")

def getAttractions (lat, lon):
	return [parseJSON(json) for json in getJSON(lat, lon, "attractions")]
	# return getJSON(lat, lon, "attractions")

def getAll (lat, lon):
	dic = {}
	dic["node"] = {"lat" : lat, "lng" : lon}
	dic["attractions"] = getAttractions(lat, lon)
	dic["food"] = getFood(lat, lon)
	dic["hotels"] = getHotels(lat, lon)
	return dic

def getResults (locations):
	return [getAll(loc["lat"], loc["lng"]) for loc in locations]
