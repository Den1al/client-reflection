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
$ sudo letsencrypt certonly -a standalone --register-unsafely-without-email
```

## Configure `run.sh` File
This app has a convenient approach to run the web application - using gunicorn. Sometimes with advances flags, `gunicorn` can be somewhat cumbersome, so I created a `run.sh` file that wraps all the desired functionalities from the tool, into a single runnable file. Create a new `run.sh` file by running the following command:
```bash
$ cp run-template.sh run.sh
```

Now, fill in the relevant information, such as youre domain name, desired log file etc. 
To run the app, first make the `run.sh` file executeable, and run it:

```bash
$ chmod +x run.sh
$ sudo ./run.sh
```


