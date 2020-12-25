import numpy as np

from io import BytesIO

from dictlogic import Logic
from flask import Flask, jsonify, request, send_file

from bob import utils

logic = Logic()

def create_app():
    app = Flask(__name__)

    from .errors import InvalidUsage
    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = 400
        return response

    from bob import transforms
    @app.route('/', methods=['POST'])
    def transform():
        payload = request.json
        if 'url' not in payload:
            raise InvalidUsage('no url')

        image = utils.fetch_image(payload['url'])
        image = logic.run(
            statement={
                'sequence': [
                    *payload.get('transforms', []),
                    {'get': 'image'},
                ]
            },
            locals={
                'image': image,
            })
        
        return send_file(BytesIO(utils.to_png(image)), mimetype='image/png')
    
    return app
