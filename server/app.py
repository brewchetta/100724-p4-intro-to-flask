#!/usr/bin/env python3

from flask import make_response, jsonify, request
from config import app

# our first request at http://localhost:5555
@app.get('/')
def index():
    return make_response( "<h1>Hello World</h1>", 404 )


# another route at http://localhost:5555/welcome
@app.get('/welcome')
def welcome():
    return make_response( "<h2>Welcome!</h2><p>This is my website...</p>", 200 )


# sending back json data
@app.get('/tv-shows')
def all_shows():
    tv_shows = [
        { "name": "Warehouse Eureka" },
        { "name": "One Piece" },
        { "name": "Teletubbies" }
    ]

    return make_response( jsonify( tv_shows ), 200 )


# handling a post request
@app.post('/tv-shows')
def post_tv_shows():
    new_show = request.json

    return f"<p>Your new show is {new_show['name']} with a rating of {new_show['rating']}</p>"


# with a parameter
@app.get('/tv-shows/<int:number_of_views>/<int:rating>')
def show_by_id(number_of_views, rating):

    return f"You're looking for a show with number of views {number_of_views} with a rating of {rating}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
