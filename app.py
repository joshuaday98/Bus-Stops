from flask import Flask, render_template, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('bus_stop.html')


@app.route('/user_address/')
def find_coords():
    import pdb; pdb.set_trace()
    geolocator = Nominatim()
    location = geolocator.geocode(users_address)
    return jsonify(lat=location.latitude, lng=longitude)

if __name__ == "__main__":
    app.run()
