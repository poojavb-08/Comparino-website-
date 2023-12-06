from flask import Flask, jsonify, request
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8', errors='replace') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

@app.route('/data', methods=['GET'])
def get_data():
    try:
        search_term = request.args.get('search', '')
        print("Search Term:", search_term)

        amazon_data = read_csv('Amazon.csv')
        flipkart_data = read_csv('Flipkart.csv')
        gem_data = read_csv('Gem.csv')

        response_data = {
            'amazon': amazon_data,
            'flipkart': flipkart_data,
            'gem': gem_data
        }

        return jsonify(response_data)
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"message": "Error"})

if __name__ == '__main__':
    app.run(debug=True)
