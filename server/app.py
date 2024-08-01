#!/usr/bin/env python3

from flask import make_response, jsonify
from config import app

@app.get('/') # GET
def index():
    return make_response( "<h1>Hello World</h1>" )

@app.get('/page-two')
def page_two():
    return make_response( "<h2>YO</h2>" )

@app.get('/some-json')
def respond_with_json():
    json_data = { 
        "name": "Bob", 
        "species": "raccoon", 
        "favFoods": ["pizza", "trash", "trash pizza"] 
    }
    return json_data, 418
    # return make_response( jsonify( json_data ), 500 )

@app.get('/raccoons/<int:id>')
def raccoon_by_id(id):
    raccoon = { "id": id, "name": "Bob" }
    # raccoon = Raccoon.query.where(Raccoon.id == id).first()
    return make_response( jsonify( raccoon ), 200 )

@app.get('/simple-addition/<int:first_num>/<int:second_num>')
def addition(first_num, second_num):
    return make_response( f"{first_num + second_num}" )

# @app.get('/hello/<string:incoming_string>')

@app.get('/greeting')
def greeting():
    return make_response( jsonify( { "response": "Hello!" } ), 200 )


@app.get('/count-to/<int:x>')
def count_to(x):

    my_list = []

    for i in range(x): # [0,1,2,3,4]
        my_list.append(i + 1)

    return make_response( jsonify( my_list ), 200 )


@app.get('/lower-case/<string:word>')
def lower_case(word):
    return make_response( jsonify( { "result": word.lower() } ), 200 )

# RESTful routes


if __name__ == '__main__':
    app.run(port=5555, debug=True)
