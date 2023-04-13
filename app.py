import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():

    # Your code for fetching the data goes here
    response = requests.get('https://manchester-airport-flights.netlify.app')
    data = response.json()
    # Renders the html and can insert the data with a second argument 'data='
    return render_template("index.html", data=data)


@app.route("/pets")
def pets():
    # Example of data being rendered in html
    data_list = [{"user": "Alex", "pets_name": "Fish"}, {
        "user": "Faz", "pets_name": "Kitty"}, {"user": "Rhiannon", "pets_name": "Rosie"}]

    return render_template("petsExample.html", data=data_list)


@app.route("/filter/<airline>")
def filtered(airline):
    print()
    # Example of data being rendered in html
    response = requests.get('https://manchester-airport-flights.netlify.app')
    data = response.json()

    filtered_data = []

    for i in data:
        if i['Airline'] == airline:
            filtered_data.append(i)


    return render_template("index.html", data=filtered_data)

if __name__ == "__main__":
    app.run()
