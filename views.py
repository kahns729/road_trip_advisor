from flask import Flask, render_template, jsonify, make_response
import sqlite3
import json

app = Flask(__name__)
app.config.from_object('config')

def access_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route("/")
def login():
    return render_template('index.html')

@app.route("/table")
def table():
    conn = access_db()
    cur = conn.execute("SELECT carrier, locality, hcpcs, nonFacFee, facFee, \
                        state, location FROM h LIMIT 1000;")
    pf15 = [dict(carrier=row[0], locality=row[1], hcpcs=row[2], \
            non_fac_fee=row[3], fac_fee=row[4], state=row[5], location=row[6]) \
            for row in cur.fetchall()]
    conn.close()
    return render_template('table.html', data=pf15)

@app.route("/smap")
def smap():
    days = [ 
            {
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
                        "location": {"lat": 41.65, "lng": -71.3}
                    }
                ],
                "end": {"lat": 41.5, "lng": -72},
                "hours_driving": 8,
                "miles": 480
            },
            {
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
                "end": {"lat": 41, "lng": -73},
                "hours_driving": 10,
                "miles": 540
            }
    ]

    return render_template('smap.html', itinerary=days)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'got rekt'}), 404)
