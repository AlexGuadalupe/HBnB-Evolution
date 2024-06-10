from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

places = []

@app.route('/places', methods=['POST'])
def create_place():
    """Create a new place."""
    data = request.json
    req_place_info = [
    {"name", "description", "address", "city_id", "latitude",
    "longitude", "host_id", "number_of_rooms", "number_of_bathrooms",
    "price_per_night", "max_guests", "amenities_ids"}
    ]
    for info in req_place_info:
        if info not in data:
            return jsonify({"message": "Missing information."}), 400
    new_place = {
        "place_id": len(places) + 1,
        "name": data["name"],
        "description": data["description"],
        "address": data["address"],
        "city_id": data["city_id"],
        "latitude": data["latitude"] ,
        "longitude": data["longitude"],
        "host_id": data ["host_id"],
        "number_of_rooms": data["number_of_rooms"],
        "number_of_bathrooms": data["number_of_batrooms"],
        "price_per_night": data["price_per_night"],
        "max_guests": data["max_guests"],
        "amenities_ids": data["amenities_ids"]
    }

    places.append(new_place)
    return jsonify({"message": "New place created with sucess."}), 201

@app.route("/places", methods=["GET"])
def get_places():
    """Get all places."""
    return jsonify(places), 200



@app.route('/places/{place_id}', methods=["GET"])
def get_place(place_id):
    """Get a specific place."""
    place = next((_place for _place in places if _place["id"] == place_id), None)
    if place is None:
        return jsonify({"error": "Place not found."}), 404
    return jsonify(place), 200


@app.route('/places/{place_id}', methods=["PUT"])
def update_place(place_id):
    data = request.json
    place = next((_place for _place in places if _place["id"] == place_id), None)
    if place is None:
        return jsonify({"error": "Place not found."}), 404
    allowed_to_change_info = [
    {"name", "description", "host_id", "number_of_rooms", "number_of_bathrooms",
    "price_per_night", "max_guests", "amenities_ids"}
    ]
    for key, value in data.items():
        if key in allowed_to_change_info:
            place[key] = value
            place["updated_at"] = datetime.now()
    for info in allowed_to_change_info:
        if info not in data:
            return jsonify({"message": "Missing information."}), 400

@app.route("/places/{place.id}", methods=["DELETE"])
def delete_place(place_id):
    """Delete a place."""
    place = next((_place for _place in places if _place["id"] == place_id), None)
    if place is None:
        return jsonify({"error": "Place not found."}), 404
    places.remove(place)
    return jsonify({"message": "Place deleted with sucess."}), 200

if __name__ == '__main__':
    app.run(debug=True)