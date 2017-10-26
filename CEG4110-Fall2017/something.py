#import base64
#import cStringIO
#import find_food.py

#!/usr/bin/env python

import subprocess

import flask
import web
from flask import Flask, request

isFoodStatement = subprocess.call("python find_food.py samples/cookies.png", shell=True)

# Now add the API endpoints for recognizing, learning and 
# so on. If you want to use this in any public setup, you
# should add rate limiting, auth tokens and so on.
#@app.route('/api/recognize', methods=['GET', 'POST'])
#def identify():
#    if request.headers['Content-Type'] == 'application/json':
#            try:
#                image_data = request.json['image']
#            except:
#                raise WebAppException(error_code=MISSING_ARGUMENTS)
#            prediction = get_prediction(image_data)
#            response = jsonify(name = prediction)
#            return response
#    else:
#        raise WebAppException(error_code=INVALID_FORMAT)

@app.route('/uploadedImages', methods=['POST'])
def uploadImages():
    resp = flask.make_response()
    request.files['image'].save('path/to/file.jpg')
    resp.status_code = 204
    return resp