import json

# Summary: returns the day itinerary by filtering out locations with
# too few reviews or too low ratings.
# Constraints: events is the return value getResults from tripadvisor.py
def getResults (data):
    data["events"] = filterEvents(data["events"], 10, 3.5)
    return makeItinerary(data)

# Summary: returns the filtered events for all waypoints 
def makeItinerary (data):
    scale = 1.5
    day = 24
    total_time = scale * data["duration"]
    locations = data["events"]
    
    for loc in locations:
        dic = {}
        dic["node"] = loc["node"]
        dic["attractions"] = filterEvents(loc["attractions"], min_review_count, min_rating)
        dic["food"] = filterEvents(loc["food"], min_review_count, min_rating)
        dic["hotels"] = filterEvents(loc["hotels"], min_review_count, min_rating)
        bestLocEvents.append(dic)
    return bestLocEvents

# Summary: returns the filtered events, removes events with
# too few reviews or too low ratings
def filterEvents(events, min_review_count, min_rating):
    bestEvents = []
    for event in events:
        #remove all events non-rated (null) and too weakly rated 
        if event["rating"] == NULL || event["rating"] < min_rating
            continue
        #remove all events with too few reviews 
        if event["num_reviews"] < min_review_count
            continue
        bestEvents.append(event)
    return bestEvents

# Summary: returns the filtered events for all waypoints 
def filterLocationEvents (locations, min_review_count, min_rating):
    bestLocEvents = []
    for loc in locations:
        dic = {}
        dic["node"] = loc["node"]
        dic["attractions"] = filterEvents(loc["attractions"], min_review_count, min_rating)
        dic["food"] = filterEvents(loc["food"], min_review_count, min_rating)
        dic["hotels"] = filterEvents(loc["hotels"], min_review_count, min_rating)
        bestLocEvents.append(dic)
    return bestLocEvents

