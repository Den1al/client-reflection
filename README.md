# client-reflection
A web application that reflects the connecting user information.

## Installation
```bash
$ pip install -r requirements.txt
```

## Usage
To run the server normally:
```bash
$ python server.py
```

To run as a daemon:
```bash
$ gunicorn server:app --workers 2 --daemon
```