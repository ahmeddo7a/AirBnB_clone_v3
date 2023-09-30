#!/usr/bin/python3
"""return the status of API"""
import os
from flask import Flask, jsonify
from flask_cors import CORS

from models import storage
from api.v1.views import app_views


app = Flask(__name__)
'''The Flask web application instance.'''
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def app_teardown(exception):
    """teardown context"""
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """404 Handler"""
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST") or "0.0.0.0"
    port = getenv("HBNB_API_PORT") or 5000
    app.run(host=host, port=port, threaded=True)
