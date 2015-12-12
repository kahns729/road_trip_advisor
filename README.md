[index]: readme/index.png
[overview]: readme/overview.png

# RoadTripAdvisor
##### [Dariusz Adamczyk](https://github.com/dariuszadamczyk), [Seth Kahn](https://github.com/kahns729), [Gabe Terrell](https://github.com/gabe-terrell) #####


Background
-----------------

TripAdvisor is a wonderful tool for flying to a specific destination; however, the service lacks a good way to plan a cross-country roadtrip, where there are dozens of possible routes along the way, all full of different sights, attractions, and food. For Tufts' Fall 2015 Polyhack, we were inspired to create RoadTripAdvisor. Given a starting location, a destination, and a desired number of driving days, RoadTripAdvisor can create an optimized road trip itinerary (food, sight-seeing, and hotels) using TripAdvisor and Google Maps APIs.

![Landing Page of RoadTripAdvisor][index]

![Itinerary for a four day road trip from Denver, CO to Somerville, MA][overview]

Usage
-----------------

The RoadTripAdvisor backend and frontend are served by the Flask framework, and are written in Python 2.7. To install the required dependencies, run `pip install -r requirements.txt`

In order to use the RoadTripAdvisor app, you must acquire API keys from TripAdvisor and Google (you must give register this key for Google Maps specifically). Once you have keys, create a **private.py** file, and inside it set the variables `GOOGLEMAPS_API_KEY` and `TRIPADVISOR_API_KEY`. These keys are used to make API calls to TripAdvisor and Google Maps.

The server is run with `python run.py`. 

Finally, open `localhost:5000` in a web browser to view the web interface for RoadTripAdvisor.
