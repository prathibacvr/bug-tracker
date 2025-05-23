from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
BUGS_FILE = 'bugs.json'

def load_bugs():
    if not os.path.exists(BUGS_FILE):
        return []
    with open(BUGS_FILE, 'r') as f:
        return json.load(f)

def save_bugs(bugs):
    with open(BUGS_FILE, 'w') as f:
        json.dump(bugs, f, indent=2)

@app.route('/bugs', methods=['GET'])
def get_bugs():
    return jsonify(load_bugs())

@app.route('/bugs/<int:bug_id>', methods=['GET'])
def get_bug(bug_id):
    bugs = load_bugs()
    for bug in bugs:
        if bug['id'] == bug_id:
            return jsonify(bug)
    return jsonify({'error': 'Bug not found'}), 404

@app.route('/bugs', methods=['POST'])
def create_bug():
    new_bug = request.json
    bugs = load_bugs()
    new_bug['id'] = len(bugs) + 1
    new_bug['status'] = 'open'
    bugs.append(new_bug)
    save_bugs(bugs)
    return jsonify(new_bug), 201

@app.route('/bugs/<int:bug_id>', methods=['PUT'])
def update_bug(bug_id):
    updated = request.json
    bugs = load_bugs()
    for bug in bugs:
        if bug['id'] == bug_id:
            bug.update(updated)
            save_bugs(bugs)
            return jsonify(bug)
    return jsonify({'error': 'Bug not found'}), 404

@app.route('/bugs/<int:bug_id>', methods=['DELETE'])
def delete_bug(bug_id):
    bugs = load_bugs()
    bugs = [bug for bug in bugs if bug['id'] != bug_id]
    save_bugs(bugs)
    return jsonify({'message': f'Bug {bug_id} deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
