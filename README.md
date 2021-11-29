# Fibonacci-API

### Running the API :

**How to run the API for development :**

```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python app.py
```
 - This will run the API on `127.0.0.0:5000`

**How to run the API in Docker :**

```
$ docker build -t fibonacci-api .
$ docker run --network host -d --name fibo fibonacci-api
```
 - This will run the API on `127.0.0.0:5000`

### Running the Testing Wab App :

**How to run the Test WebApp :** 

Always inside the virtual environment :
```
$ python tests/WebTester.py
```
 - This will run the test server on `localhost:8000`

### Running the Unit Tests :

Inside the virtual environment :
```
$ pytest
```
