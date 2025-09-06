from pyedhrec import EDHRec
from flask import Flask, render_template, redirect, url_for
import csv

app = Flask(__name__)
edhrec = EDHRec()

@app.route("/")
def home():
    return render_template("index.html")

def high_syn(cardName, collection):
    print("")
    cards = edhrec.get_high_synergy_cards(cardName)["High Synergy Cards"]
    print("You own the following high synergy cards: \n")
    for card in cards:
        if card["name"] in collection:
            print(card["name"] + "\n" + card["label"] + "\n")

def top(cardName, collection):
    print("")
    cards = edhrec.get_top_cards(cardName)["Top Cards"]
    print("You own the following top cards: \n")
    for card in cards:
        if card["name"] in collection:
            print(card["name"] + "\n" + card["label"] + "\n")

def console():

    archCSVFile = "data.csv"

    collection = []

    with open(archCSVFile, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            collection.append(row[0])

    cardName = input("\nPlease input a card name: ")

    creatures = edhrec.get_top_creatures(cardName)

    instants = edhrec.get_top_instants(cardName)

    sorceries = edhrec.get_top_sorceries(cardName)

    enchant = edhrec.get_top_enchantments(cardName)

    mana_art = edhrec.get_top_mana_artifacts(cardName)

    battles = edhrec.get_top_battles(cardName)

    planes = edhrec.get_top_planeswalkers(cardName)

    util = edhrec.get_top_utility_lands(cardName)

    lands = edhrec.get_top_lands(cardName)

    high_syn(cardName, collection)
    top(cardName, collection)

if __name__ == "__main__":
    app.run(debug=False)
    console() #Will only run if server is closed with CTRL-C first