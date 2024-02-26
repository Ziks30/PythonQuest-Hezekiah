from flask import Flask, jsonify
import csv

app = Flask(__name__)

csv_file = 'programming_languages.csv'

def read_csv():
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

        return data

@app.route('/', methods=['GET'])
def get_langs():
    content = read_csv()
    return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)