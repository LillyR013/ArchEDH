from pyedhrec import EDHRec
from flask import Flask, render_template, send_from_directory
import os

from requests import HTTPError

app = Flask(__name__)
edhrec = EDHRec()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/commanderSuggestion")
def suggest():
    return render_template("commanderSuggestion.html")

@app.route("/commander/<commander>")
def search(commander):
    try:
        cardData = edhrec.get_card_details(commander)
        return cardData
    except HTTPError:
        return {'error': 'Invalid Card'}
    
@app.route("/creatures/<commander>")
def top_creatures(commander):
    try:
        cardData = edhrec.get_top_creatures(commander)
        return cardData
    except HTTPError:
        return {'error': 'Invalid Card'}
    
@app.route("/top/<commander>")
def top_cards(commander):
    try:
        cardData = edhrec.get_top_cards(commander)
        return cardData
    except HTTPError:
        return {'error': 'Invalid Card'}

if __name__ == "__main__":
    app.run(debug=False)