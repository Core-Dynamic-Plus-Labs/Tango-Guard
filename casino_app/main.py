# File: casino_app/main.py
from flask import Flask, request, jsonify
from models import init_db, add_exclusion, get_exclusion_by_id_number, view_exclusions
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
init_db(app)

@app.route('/')
def index():
    return "Welcome to the Casino Involuntary Exclusion List API"

@app.route('/exclusions', methods=['POST'])
def add_exclusion_api():
    data = request.get_json()
    try:
        add_exclusion(data)
        return jsonify({'message': 'Exclusion added successfully'}), 201
    except IntegrityError:
        return jsonify({'message': 'Exclusion with this ID number already exists'}), 400

@app.route('/exclusions/<id_number>', methods=['GET'])
def get_exclusion_api(id_number):
    exclusion = get_exclusion_by_id_number(id_number)
    if exclusion:
        exclusion_data = {
            'id': exclusion.id,
            'name': exclusion.name,
            'date_of_birth': exclusion.date_of_birth,
            'gender': exclusion.gender,
            'street': exclusion.street,
            'city': exclusion.city,
            'state': exclusion.state,
            'zip': exclusion.zip,
            'reason': exclusion.reason,
            'start_date': exclusion.start_date,
            'end_date': exclusion.end_date,
            'exclusion_authority': exclusion.exclusion_authority,
            'notes': exclusion.notes,
            'id_type': exclusion.id_type,
            'id_number': exclusion.id_number
        }
        return jsonify(exclusion_data)
    else:
        return jsonify({'message': 'Exclusion not found'}), 404

@app.route('/exclusions', methods=['GET'])
def view_exclusions_api():
    exclusions = view_exclusions()
    exclusion_list = []
    for exclusion in exclusions:
        exclusion_list.append({
            'id': exclusion.id,
            'name': exclusion.name,
            'date_of_birth': exclusion.date_of_birth,
            'gender': exclusion.gender,
            'street': exclusion.street,
            'city': exclusion.city,
            'state': exclusion.state,
            'zip': exclusion.zip,
            'reason': exclusion.reason,
            'start_date': exclusion.start_date,
            'end_date': exclusion.end_date,
            'exclusion_authority': exclusion.exclusion_authority,
            'notes': exclusion.notes,
            'id_type': exclusion.id_type,
            'id_number': exclusion.id_number
        })
    return jsonify(exclusion_list)

if __name__ == '__main__':
    app.run(debug=True)
