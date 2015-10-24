from flask import Flask, render_template, jsonify, make_response
import sqlite3
import json

app = Flask(__name__)
app.config.from_object('config')

days = [ 
            {
                "day": 1,
                "start": {"lat": 42, "lng": -71},
                "events": [
                    {
                        "name": "Event 1",
                        "category": {"name": "hotel"},
                        "location": {"lat": 43, "lng": -70}
                    },
                    {
                        "name": "Event 2",
                        "category": {"name": "attraction"},
                        "location": {"lat": 44, "lng": -69}
                    },
                    {
                        "name": "Event 3",
                        "category": {"name": "food"},
                        "location": {"lat": 45, "lng": -68}
                    }
                ],
                "end": {"lat": 45, "lng": -68},
                "hours_driving": 8,
                "miles": 480
            },
            {
                "day": 2,
                "start": {"lat": 45, "lng": -68},
                "events": [
                    {
                        "name": "Day 2 Event 1",
                        "category": "Hotel",
                        "location": {"lat": 44, "lng": -69}
                    },
                    {
                        "name": "Day 2 Event 2",
                        "category": "Attraction",
                        "location": {"lat": 43, "lng": -70}
                    },
                    {
                        "name": "Day 2 Event 3",
                        "category": "Food",
                        "location": {"lat": 42, "lng": -71}
                    }
                ],
                "end": {"lat": 42, "lng": -71},
                "hours_driving": 10,
                "miles": 540
            }
    ]

def access_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route("/trip")
def trip():
    return render_template('trip.html', days=days)

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

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'not found'}), 404)
