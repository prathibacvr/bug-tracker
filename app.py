from flask import Flask, jsonify, request, send_from_directory
import json
import os

app = Flask(__name__)

BUGS_FILE = 'bugs.json'

def load_bugs():
    if not os.path.exists(BUGS_FILE):
        return []
    with open(BUGS_FILE, 'r') as file:
        return json.load(file)

def save_bugs(bugs):
    with open(BUGS_FILE, 'w') as file:
        json.dump(bugs, file, indent=4)

# Serve frontend HTML page
@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

# Get all bugs
@app.route('/bugs', methods=['GET'])
def get_bugs():
    return jsonify(load_bugs()), 200

# Create a new bug
@app.route('/bugs', methods=['POST'])
def create_bug():
    bugs = load_bugs()
    data = request.get_json()
    
    required_fields = ['title', 'description', 'severity']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    new_bug = {
        'id': bugs[-1]['id'] + 1 if bugs else 1,
        'title': data['title'],
        'description': data['description'],
        'severity': data['severity'],
        'status': 'open'
    }
    bugs.append(new_bug)
    save_bugs(bugs)
    return jsonify(new_bug), 201

# Update bug status (e.g., mark as resolved)
@app.route('/bugs/<int:bug_id>', methods=['PUT'])
def update_bug(bug_id):
    bugs = load_bugs()
    data = request.get_json()
    for bug in bugs:
        if bug['id'] == bug_id:
            bug['status'] = data.get('status', bug['status'])
            save_bugs(bugs)
            return jsonify(bug), 200
    return jsonify({'error': 'Bug not found'}), 404

# Delete a bug
@app.route('/bugs/<int:bug_id>', methods=['DELETE'])
def delete_bug(bug_id):
    bugs = load_bugs()
    updated_bugs = [bug for bug in bugs if bug['id'] != bug_id]
    if len(updated_bugs) == len(bugs):
        return jsonify({'error': 'Bug not found'}), 404
    save_bugs(updated_bugs)
    return jsonify({'message': 'Bug deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
