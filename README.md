# Flask project with designing own APIs
The following repo is a flask project where we design our own APIs. Flask is a framework which maps HTTP requests to Python functions. Helping you view functions as a HTML page.

### Prerequisites
There are two API scripts, one is without the SQLite3 library
View the first script as an introductory script before seeing the other api_final.py

## Flask: A Primer 
Flask is a Python framework for web applications. Simply put, it displays function output/logic in HTML format. 
Think of every function as a view and Flask creates a route so essentially a url and displays the function which is mapped to the route, as a html outpout.
Routes are the little decorator that you would see above your function
```
@app.route('/', methods=['GET'])
```
This route would be your homepage and be mapped to whatever function below. 
Eg)
```
@app.route('/', methods=['GET'])
def test():
    return ("Hello world!")
```
