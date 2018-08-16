from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        user_agent=request.headers.get('User-Agent'),
        ip=request.remote_addr,
        headers=dict(request.headers)
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
