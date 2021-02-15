''' How to develop this: 
Search for book based on title, author, year, etc. 
How to add a book to the collection
How to remove etc. 
'''
# Flask maps HTTP requests to Python functions
import flask
from flask import request, jsonify

# App is an instance of the Flask, taking in the __name__ of the script file :
app = flask.Flask(__name__) 
app.config["DEBUG"] = True

# A List of Dictionaries 
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
     
     {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

# Maps it to the home function to return a string on a html webpage
@app.route('/', methods=['GET'])
def home():
    # Returns html markup 
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>" 


# A route to return all the available entries in our catalog, constructing our api endpoint.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    # Returns books list datastructure in JSON format in HTML markup
    return jsonify(books)

# App route is mapped to the url below so you combine that with 127.0.0.1 etc.
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL
    # If ID is provided assign it to a variable
    # If no ID is provided, display an error in the browser

    if 'id' in request.args:
    # request.args = request arguments from http? 
        id = int(request.args['id'])
    else:
        return "Error: no id field provided. Please specify an id."

    results = []
    
    # Loop through the data and match results that fit the requested ID
    # IDs are unique but other fields might return many results

    for book in books:
        if book['id'] == id:
            results.append(book)

    # Jsonify function from Flask to convert our list of Python dictionaries to JSON format

    return jsonify(results)
app.run()
