"""
 Application of Programming Principles
 Assignment Template 2021-22 - Flask & Python
 
"""
from flask import Flask, render_template, jsonify, request, make_response
import sys, json, os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


#Joke functions


@app.route("/api/jokes", methods=['GET'])
def joke():
    """
    This function reads the entries in the file containing the joke entries in the data folder.
    It then formats the result into a JSON response object and returns the JSON response object.
    """
    site_root = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(site_root, "data", "jokes.json")

    #With keyword deals with closing file etc.
    with open(json_url, 'r') as openfile:
        #Reading from json file
        json_object = json.load(openfile)
    return json_object


@app.route("/api/jokes", methods=['PUT'])
def upload():
    """
    This function receives a new joke entries list from the website DOM. It then formats the
    result into a .json file of the same name and overwrites the one on the system, effectively
    updating the stored jokes list.
    """
    print('saving Jokes')
    messageOK = jsonify(message="Jokes uploaded!")
    messageFail = jsonify(
        message="Uploading Jokes failed as data not in JSON format!")
    if request.is_json:
        #Parse the JSON into a Python dictionary
        req = request.get_json()
        #Print the dictionary
        print(req)
        #Save json to file
        site_root = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(site_root, "data", "jokes.json")

        #with keyword deals with closing file etc.
        with open(json_url, 'w') as openfile:
            json.dump(req, openfile)

        #Return a string along with an HTTP status code
        return messageOK, 200

    else:

        #The request body wasn't JSON so return a 400 HTTP status code
        return messageFail, 400


#Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)