import json
from flask import Flask, jsonify

data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35}
]
app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 35}
    ]

    # Use json.dumps to serialize the data into JSON format
    json_data = json.dumps(data)

    # Return the serialized data in a JSON response
    return jsonify(json.loads(json_data))  # Converting back to JSON object for Flask

if __name__ == '__main__':
    app.run(debug=True)
