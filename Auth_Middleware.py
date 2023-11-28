from flask import Flask, jsonify, make_response, request
from functools import wraps

import json

f = open('tokens.json')
 
tokens = json.load(f)["tokens"]
 
f.close()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')
        if auth_header:
                try:
                    auth_token = auth_header.split(" ")[1]
                    if auth_token not in tokens:
                        responseObject = {
                            'status': 'fail',
                            'message': 'Bearer token malformed.'
                        }
                        return make_response(jsonify(responseObject)), 401
                except IndexError:
                    responseObject = {
                        'status': 'fail',
                        'message': 'Bearer token malformed.'
                    }
                    return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Bearer token malformed.'
            }
            return make_response(jsonify(responseObject)), 401
            
        return f(*args, **kwargs)
    return decorated