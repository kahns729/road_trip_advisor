import os, private
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'dat_data.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'i7waonvewRRi6U'
DATABASE_PATH = os.path.join(basedir, DATABASE)

# Google Maps API
GOOGLEMAPS_API_KEY = private.GOOGLEMAPS_API_KEY
DIST_INTERVAL = 40 #miles

# Trip Advisor API
LOCATION_RADIUS = 10 
TRIPADVISOR_API_KEY = private.TRIPADVISOR_API_KEY