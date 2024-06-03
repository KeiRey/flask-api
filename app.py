from flask import Flask, jsonify
import os, json, uuid
import requests

db = json.load(open('data.json'))
app = Flask(__name__)

response_data = {
    'code': '00',
    'message': 'Success get data',
    'data': []
}

@app.route('/', methods=['GET'])
def get_data():
    pokeapi_url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(pokeapi_url)
    data = response.json()
    json.dump(data, open('data.json', 'w'), indent=4)
    response_data['data'] = data
    return jsonify(response_data)

@app.route('/<int:id>', methods=['GET'])
def get_data_by_id(id):
    pokeapi_url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(pokeapi_url)
    data = response.json()
    response_data['data'] = data
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

