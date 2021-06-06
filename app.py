from flask import Flask, render_template, jsonify, redirect
import json

app = Flask(__name__, static_url_path='/static/')

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/map', methods=['GET'])
def map():
    return render_template("map.html")

def return_my_coordinates():
    # Read the file
    my_coordinates = open("static/heatmap.txt").read()
    # Split each coordinate on new line
    new_line_character = "\n"
    return my_coordinates.split(new_line_character)

@app.route('/geojson')
def geojson():
    features = []
    counts = {}
    for val in return_my_coordinates():
        if val not in counts:
            counts[val] = 0
        counts[val] += 1

    for key, count in counts.items():
        longitude, latitude = [float(x) for x in key.split(",")]
        features.append({ "type": "Feature", "properties": { "id": key, "mag": count }, "geometry": { "type": "Point", "coordinates": [ longitude, latitude, 1.0 ] } })
    
    return jsonify({
        "type": "FeatureCollection",
        "crs": { "type": "name", "properties": { "name": "heatmap" } },
        "features": features
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)