from uuid import uuid4
from flask import (Flask, render_template, request,
                   redirect, url_for, make_response)

app = Flask(__name__)


def generate_uuid():
    return str(uuid4())

# def parsed_cookie():
#     for item in request.headers.get('Cookie').split(';'):
#         name, _, value = item.partition('=')
#         yield name, value


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

    resp.set_cookie('cookie2', generate_uuid())
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=31337, debug=True)
