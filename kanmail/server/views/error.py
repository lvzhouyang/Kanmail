from flask import jsonify, make_response

from kanmail.log import logger
from kanmail.server.app import app


@app.errorhandler(400)
def error_bad_request(e):
    return make_response(jsonify(
        status_code=e.code,
        error_name=e.name,
        error_message=e.description,
    ), 400)


@app.errorhandler(404)
def error_not_found(e):
    return make_response(jsonify(
        status_code=e.code,
        error_name=e.name,
        error_message=e.description,
    ), 404)


@app.errorhandler(405)
def error_method_not_allowed(e):
    return make_response(jsonify(
        status_code=e.code,
        error_name=e.name,
        error_message=e.description,
    ), 405)


@app.errorhandler(Exception)
def error_unexpected_exception(e):
    error_name = e.__class__.__name__
    message = f'{getattr(e, "args", e)}'

    # Re-raise it so we log it
    try:
        raise e
    except Exception:
        logger.exception(f'Unexpected exception in view: {message}')

    return make_response(jsonify(
        status_code=500,
        error_name=error_name,
        error_message=message,
    ), 500)
