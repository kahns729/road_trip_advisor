import json, config
from math import ceil

# Summary: returns the day itinerary by filtering out locations with
#          too few reviews or too low ratings.
# Constraints: events is the return value getResults from tripadvisor.py
def getResults (data):
    locations = data["events"]
    bestLocEvents = []
    min_num_events = 10
    for loc in locations:
        dic = {}
        dic["node"] = loc["node"]
        dic["attractions"] = filterEvents(loc["attractions"], min_num_events)
        dic["food"] = filterEvents(loc["food"], min_num_events)
        dic["hotels"] = filterEvents(loc["hotels"], min_num_events)
        bestLocEvents.append(dic)
    data["events"] = bestLocEvents
    return makeItinerary(data)

# Summary: returns the filtered events for all waypoints 
def makeItinerary (data):
    scale = 1.5
    daytime = 12
    user_desired_days = data["usertime"]
    min_time = data["duration"]
    total_time = int(ceil(scale * data["duration"]))
    fun_time = int(ceil(user_desired_days * daytime)) - total_time
    num_activities = fun_time / 2
    locations = data["events"]
    drive_hours = int(ceil(user_desired_days * daytime)) - fun_time

    # number of locations we pass in a day
    interval = int(ceil(length(locations) / user_desired_days))
    # if an edge case, no activities fit into schedule
    if edge_case(user_desired_days, min_time, num_activities):
        return []
    for i in range(num_activities):
        temp = []
        # for each location in the day interval
        for j in range(interval):
            # if out of bounds
            if i + j >= length(locations):
                break;
            temp.append(locations[i + j])
        bestDay = reduce(findBest, temp, [])
    
    # select top 1 from each interval
    # take (num_activites - user_desired_days)
    return bestLocEvents

# Summary: returns true if an edge case
def edge_case (user_days, min_hours, num_activities):
    if user_days * 24 <= int(ceil(min_hours)):
        return True
    elif num_activities < user_days:
        return True
    return False

 # Summary: returns the filtered events for all waypoints 
def filterEvents (events, min_num_events):
    bestEvents = []
    choose_best = create_filterEvent(min_num_events)
    return reduce(choose_best, events, bestEvents)
    
# Summary: returns the filtered events, removes events with
#          too few reviews or too low ratings
def create_filterEvent(min_num_events):
    def filterEvent(bestEvents, event):
        if length(bestEvents) < min_num_events:
            bestEvents.append(event)
        else:
            bestEvents.append(event)
            bestEvents.remove(worstBestEvent(bestEvents)])
        return bestEvents

# Summary: returns the best event with the fewest number of reviews
def worstBestEvent(events):
    minimum = {}
    count = 0
    for event in events:
        if count == 0
            minimum = event
        elif minimum["num_reviews"] > event["num_reviews"]:
            minimum = event
    return minimum




