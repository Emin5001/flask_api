from flask import request
from app import app

@app.route('/hello', methods=['GET'])    
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe.'
    