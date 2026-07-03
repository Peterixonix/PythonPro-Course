from flask import jsonify


def http_err(msg, code):
    return jsonify({"error": msg}), code
