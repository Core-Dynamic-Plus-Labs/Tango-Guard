from flask import Flask, request, jsonify
from models import init_db, add_exclusion, get_exclusion_by_id_number, view_exclusions

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return "Welcome to the Casino Involuntary Exclusion List API"

@app.route('/exclusions', methods=['POST'])
def add_exclusion_api():
    data = request.get_json()
    add_exclusion(data)
    return jsonify({'message': 'Exclusion added successfully'}), 201

@app.route('/exclusions/<id_number>', methods=['GET'])
def get_exclusion_api(id_number):
    exclusion = get_exclusion_by_id_number(id_number)
    if exclusion:
        exclusion_data = {
            'id': exclusion[0],
            'name': exclusion[1],
            'date_of_birth': exclusion[2],
            'gender': exclusion[3],
            'street': exclusion[4],
            'city': exclusion[5],
            'state': exclusion[6],
            'zip': exclusion[7],
            'reason': exclusion[8],
            'start_date': exclusion[9],
            'end_date': exclusion[10],
            'exclusion_authority': exclusion[11],
            'notes': exclusion[12],
            'id_type': exclusion[13],
            'id_number': exclusion[14]
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
            'id': exclusion[0],
            'name': exclusion[1],
            'date_of_birth': exclusion[2],
            'gender': exclusion[3],
            'street': exclusion[4],
            'city': exclusion[5],
            'state': exclusion[6],
            'zip': exclusion[7],
            'reason': exclusion[8],
            'start_date': exclusion[9],
            'end_date': exclusion[10],
            'exclusion_authority': exclusion[11],
            'notes': exclusion[12],
            'id_type': exclusion[13],
            'id_number': exclusion[14]
        })
    return jsonify(exclusion_list)

if __name__ == '__main__':
    app.run(debug=True)
