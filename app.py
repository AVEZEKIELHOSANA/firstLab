  
from flask import Flask, jsonify

app = Flask(_name_)


@app.route('/')
def home():
    return jsonify(message="Hello level 400 FET, Quality Assurance!")


if _name_ == '_main_':
    app.run(debug=True)
