from pyedhrec import EDHRec
import csv

edhrec = EDHRec()
archCSVFile = "data.csv"

def high_syn(cardName):
    print("")
    cards = edhrec.get_high_synergy_cards(cardName)["High Synergy Cards"]
    print("You own the following high synergy cards: \n")
    for card in cards:
        if card["name"] in collection:
            print(card["name"] + "\n" + card["label"] + "\n")

def top(cardName):
    print("")
    cards = edhrec.get_top_cards(cardName)["Top Cards"]
    print("You own the following top cards: \n")
    for card in cards:
        if card["name"] in collection:
            print(card["name"] + "\n" + card["label"] + "\n")

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

high_syn(cardName)
top(cardName)

#print()
#print(top)
#print()
#print(creatures)
#print()
#print(instants)
#print()
#print(sorceries)
#print()
#print(enchant)
#print()
#print(mana_art)
#print()
#print(battles)
#print()
#print(planes)
#print()
#print(util)
#print()
#print(lands)

