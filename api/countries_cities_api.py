from flask import Blueprint, jsonify, request
from datetime import datetime

countries_cities_blueprint = Blueprint('countries&cities_api', __name__)
cities = []
countries = []


@countries_cities_blueprint.route('/countries', methods=['GET'])
def get_countries():
    """Get all pre-loaded countries"""
    return jsonify(countries), 200


@countries_cities_blueprint.route('/countries/{country_code}', methods=['GET'])
def get_country_info(country_code):
    """Get information of a specific country ."""
    country = next(
        (_country for _country in countries if _country["code"] == country_code), None)
    if country is None:
        return jsonify({"error": "Country not found."}), 404
    return jsonify(country), 200


@countries_cities_blueprint.route('/countries/{country_code}', methods=['GET'])
def get_country(country_code):
    """Get a specific country."""
    country = next(
        (_country for _country in countries if _country["code"] == country_code), None)
    if country is None:
        return jsonify({"error": "Country not found."}), 404
    return jsonify(country), 200


@countries_cities_blueprint.route('/countries/{country_code}/cities', methods=['GET'])
def get_cities_of_country(country_code):
    """Get all cities of a specific country."""
    country = next(
        (_country for _country in countries if _country["code"] == country_code), None)
    if country is None:
        return jsonify({"error": "Country not found."}), 404
    return jsonify(country["cities"]), 200


@countries_cities_blueprint.route('/city', methods=['POST'])
def create_city():
    """Create a new city."""
    data = request.json
    req_city_info = [
        {"name", "code"}
    ]

    for info in req_city_info:
        if info not in data:
            return jsonify({"message": "Missing information."}), 400

    new_city = {"id": len(cities) + 1,
                "name": data["name"],
                "code": data["code"]
                }

    cities.append(new_city)
    return jsonify({"message": "New city created with sucess."}), 201


@countries_cities_blueprint.route('/cities', methods=['GET'])
def get_cities():
    """Get all cities."""
    return jsonify(cities), 200


@countries_cities_blueprint.route('/cities/{city_id}', methods=['GET'])
def update_city(city_id):
    """Update a city."""
    data = request.json
    city = next((_city for _city in cities if _city["id"] == city_id), None)
    if city is None:
        return jsonify({"error": "City not found."}), 404
    allowed_to_change_info = [
        {"name", "code"}
    ]
    for key, value in data.items():
        if key in allowed_to_change_info:
            city[key] = value
            city["updated_at"] = datetime.now()
    for info in allowed_to_change_info:
        if info not in data:
            return jsonify({"message": "Missing information."}), 400


@countries_cities_blueprint.route('/cities/{city_id}')
def delete_city(city_id):
    """Delete a city."""
    city = next((_city for _city in cities if _city["id"] == city_id), None)
    if city is None:
        return jsonify({"error": "City not found."}), 404
    cities.remove(city)
    return jsonify({"message": "City deleted with sucess."}), 200
