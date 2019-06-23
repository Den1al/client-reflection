import os
from uuid import uuid4
import logging
from flask import (Flask, render_template, request,
                   redirect, url_for, make_response)

app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


@app.before_request
def log_headers():
    app.logger.debug('Request Headers: \n%s', request.headers)
    app.logger.debug('Data: \n%s', request.get_data())


def generate_uuid():
    return str(uuid4())


@app.route('/')
def index():
    resp = make_response(redirect(url_for('after_cookie_was_set')))
    resp.set_cookie('client-reflection-cookie', generate_uuid())
    return resp


@app.route('/after-cookie-was-set')
def after_cookie_was_set():
    resp = make_response(render_template(
        'index.html',
        user_agent=request.headers.get('User-Agent'),
        ip=request.remote_addr,
        headers=dict(request.headers)
    ))

    resp.set_cookie('other-cookie', generate_uuid())

    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT') or 31337)
