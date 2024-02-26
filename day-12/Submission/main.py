from flask import Flask, jsonify  

app = Flask(__name__)

my_info = {
    "name": "Hezekiah Glenn Gutay",
    "course_and_section": "BSIT 2-5",
    "favorite_programming language": "Python",
    "aws_service": "Amazon EC2",
}

@app.route("/", methods=["GET"])
def get_info():
    return jsonify(my_info)

if __name__ == "__main__":
    app.run(debug=True)