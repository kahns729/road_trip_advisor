import urllib2, json

API_KEY  = "A43BE80DF04A4F98A60B76E42CF05D7F"
API_KEY2 = "EB205D5CF19247E3BC975276040A7687"

def getJSON (lat, lon, extra = None):
	address = "http://api.tripadvisor.com/api/partner/2.0/map/"
	address += str(lat) + "," + str(lon)
	if extra:
		address += "/" + extra
	address += "?key=" + API_KEY
	JSON = json.loads(urllib2.urlopen(address).read())
	return JSON['data']

def parseJSON (json):
	dic = {}
	dic["address"] = json["address_obj"]["address_string"]
	dic["dist"] = float(json["distance"])
	dic["lat"] = float(json["latitude"])
	dic["lng"] = float(json["longitude"])
	dic["name"] = json["name"]
	return dic

def getFood (lat, lon):
	return [parseJSON(json) for json in getJSON(lat, lon, "restaurants")]

def getHotels (lat, lon):
	return [parseJSON(json) for json in getJSON(lat, lon, "hotels")]

def getAttractions (lat, lon):
	return [parseJSON(json) for json in getJSON(lat, lon, "attractions")]

def getAll (lat, lon):
	dic = {}
	dic["node"] = {"lat" : lat, "lng" : lng}
	dic["attractions"] = getAttractions(lat, lon)
	dic["food"] = getFood(lat, lon)
	dic["hotels"] = getHotels(lat, lon)
	return dic

def getResults (locations):
	return [getAll(loc["lat"], loc["lng"]) for loc in locations]
