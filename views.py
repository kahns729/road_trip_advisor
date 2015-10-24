import path, tripadvisor, itinerary
from flask import Flask, render_template, jsonify, make_response, request
import sqlite3
import json

days = [ 
            {
                "day": 1,
                "start": {"lat": 42, "lng": -71},
                "events": [
                    {
                        "name": "Event 1",
                        "category": {"name": "hotel"},
                        "location": {"lat": 41.7, "lng": -71.5}
                    },
                    {
                        "name": "Event 2",
                        "category": {"name": "attraction"},
                        "location": {"lat": 41.6, "lng": -71.8}
                    },
                    {
                        "name": "Event 3",
                        "category": {"name": "food"},
                        "location": {"lat": 41.65, "lng": -71.5}
                    }
                ],
                "end": {"lat": "41.5", "lng": "-72"},
                "hours_driving": 8,
                "miles": 480
            },
            {
                "day": 2,
                "start": {"lat": 41.5, "lng": -72},
                "events": [
                    {
                        "name": "Day 2 Event 1",
                        "category": "Hotel",
                        "location": {"lat": 41.3, "lng": -72.3}
                    },
                    {
                        "name": "Day 2 Event 2",
                        "category": "Attraction",
                        "location": {"lat": 41.5, "lng": -72.5}
                    },
                    {
                        "name": "Day 2 Event 3",
                        "category": "Food",
                        "location": {"lat": 41.8, "lng": -72.8}
                    }
                ],
                "end": {"lat": 41, "lng": -72.2},
                "hours_driving": 10,
                "miles": 540
            }
    ]

app = Flask(__name__)
app.config.from_object('config')

@app.route("/smap")
def smap():
    return render_template('smap.html', itinerary=days)

def access_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route("/trip")
def trip():
    start = request.args.get('start', None)
    end = request.args.get('end', None)
    trip_length = request.args.get('trip_length', None)
    if trip_length == None:
       trip_length = 0 
    print("Start loc: " + start + "\nEnd loc: " + end)
    nodes = path.find_waypoints(start, end, trip_length)
    # nodes = path.find_waypoints("USS Alabama, Battleship Parkway, Mobile, AL", "USS Constitution, Boston, MA")
    events = tripadvisor.getResults(nodes)
    yodays = itinerary.getResults(events)
    return render_template('trip.html', days=yodays)


@app.route("/")
def login():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'got rekt'}), 404)
