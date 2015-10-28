Background
-----------------

This repository contains the 2015 Tufts PolyHack project *RoadTripAdvisor*. The project is intended to showcase the use of the TripAdvisor API and the Google Maps API, and some complex algorithms for connecting the two together in an interesting way.


Usage
-----------------

The RoadTripAdvisor backend and frontend are served by the Flask framework, and are written in Python 2.7. To install the required dependencies, run `pip install -r requirements.txt`

In order to use the RoadTripAdvisor app, you must acquire API keys from TripAdvisor and Google (you must give register this key for Google Maps specifically). Once you have keys, create a **private.py** file, and inside it set the variables `GOOGLEMAPS_API_KEY` and `TRIPADVISOR_API_KEY`. These keys are used to make API calls to TripAdvisor and Google Maps.

The server is run with `python run.py`. 

Finally, open `localhost:5000` in a web browser to view the web interface for RoadTripAdvisor.