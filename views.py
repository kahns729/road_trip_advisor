import path, tripadvisor, itinerary
from flask import Flask, render_template, jsonify, make_response, request
import sqlite3
import json

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
    print("Start loc: " + start + "\nEnd loc: " + end + "\nTrip len: " + str(trip_length))
    nodes = path.find_waypoints(start, end, trip_length)
    # nodes = path.find_waypoints("USS Alabama, Battleship Parkway, Mobile, AL", "USS Constitution, Boston, MA")
    events = tripadvisor.getResults(nodes)
    days = itinerary.getResults(events)
    return render_template('trip.html', days=days)


@app.route("/")
def login():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'got rekt'}), 404)
