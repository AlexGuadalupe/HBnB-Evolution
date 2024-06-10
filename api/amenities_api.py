from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

amenities = []

@app.route('/ammenities', methods=['POST'])
def create_amenity():
    """Create a new amenity"""
    data = request.json
    req_amenity_info = [
    {"name"}
    ]

    for info in req_amenity_info:
        if info not in data:
            return jsonify({"message": "Missing information."}), 400

    new_amenity = {"id":len(amenities) + 1["id"],
    "name":data["name"],
    "created_at":datetime.datetime["created_at"],
    "updated_at":datetime.datetime["updated_at"]

    }

    amenities.append(new_amenity)
    return jsonify({"message": "New amenity created with sucess."}), 201

@app.route('/ammenities', methods=['GET'])
def get_amenities():
    """Get all amenities."""
    return jsonify(amenities), 200

@app.route('/ammenities/{amenity_id}', methods=['GET'])
def get_amenity(amenity_id):
    """Get a specific amenity."""
    amenity = next((_amenity for _amenity in amenities if _amenity["id"] == amenity_id), None)
    if amenity is None:
        return jsonify({"error": "Amenity not found."}), 404
    return jsonify(amenity), 200

@app.route('/ammenities/{amenity_id}', methods=['PUT'])
def update_amenity(amenity_id):
    """Update an amenity."""
    data = request.json
    amenity = next((_amenity for _amenity in amenities if _amenity["id"] == amenity_id), None)
    if amenity is None:
        return jsonify({"error": "Amenity not found."}), 404
    allowed_to_change_info = [
    {"name"}
    ]
    for key, value in data.items():
        if key in allowed_to_change_info:
            amenity[key] = value
            amenity["updated_at"] = datetime.now()
    for info in allowed_to_change_info:
        if info not in data:
            return jsonify({"message": "Missing information."}), 400


@app.route('/ammenities/{amenity_id}', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Delete an amenity."""
    amenity = next((_amenity for _amenity in amenities if _amenity["id"] == amenity_id), None)
    if amenity is None:
        return jsonify({"error": "Amenity not found."}), 404
    amenities.remove(amenity)
    return jsonify({"message": "Amenity deleted with sucess."}), 200