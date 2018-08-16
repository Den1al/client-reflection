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

## Let's Encrypt
In order to setup a ceritifcate for the app simply run let's encrypt:
```bash
$ sudo apt-get update
$ sudo apt-get install letsencrypt
$ sudo letsencrypt certonly -a standalone
```

Then generate the certs:
```bash
$ sudo letsencrypt certonly -a standalone
```

Now the certs will reside in `/etc/letsencrypt/live/<DOMAIN>/`. Let's run gunicorn with the new certs:
```bash
gunicorn server:app --workers 2 --daemon --bind 0.0.0.0:443 --keyfile /etc/letsencrypt/live/<DOMAIN>/privkey.pem --certfile /etc/letsencrypt/live/<DOMAIN>/cert.pem --ca-certs /etc/letsencrypt/live/<DOMAIN>/chain.pem --access-logfile /root/client-reflection/access.log
```