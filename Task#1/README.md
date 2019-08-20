# Task ID: Google/Facebook/Github_Auth

Dependencies: 
Flask - micro webframework in Python.
oauthlib  - framework that provides OAuth
pyOpenSSL - module build on top of OpenSSL library and helps us to call a OpenSSL library functions.
(Used in this project for "https")

Flask-Login - module that provides user session management(log in, log out,...)

Setup:

Create a new python environment into the main cloned repo directory.

```
python3 -m venv <environmentname>
```

Install the dependencies listed in 'requirements.txt'
```
pip install -r requirements.txt
```

Run below command twice to initialize database and host the Flask server locally.
```
python app.py
```

Links/Docs reffered:
```
https://realpython.com/python-virtual-environments-a-primer/
```
```
https://realpython.com/flask-google-login/
```
https://github.com/realpython/materials/tree/master/flask-google-login
```



