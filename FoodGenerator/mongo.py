from pymongo import MongoClient
from datetime import datetime
from FoodGenerator.views import *


client = MongoClient("mongodb+srv://rba:Deutschland100@cluster0.9paclpl.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('rezepte_db')
records = db.rezepte_lastsearch
rec = records.count_documents({})
print("Anzahl Docs: " +str(rec))

def addlastsearch(rezept,name,ingredients,instructions,vorauswahl_filter):
    print("in Upload__________")
    print(rezept)
    print("_______-")
    print(vorauswahl_filter)
    uploaddoc = {
        'rezept': name,
        'Zutaten': ingredients,
        'Beschreibung': instructions,
        'tags' : vorauswahl_filter,

    }
    records.insert_one(uploaddoc)

    return

def downloadlastadd():
    print("in Download")
    documents = records.find().sort('timestamp', 1).limit(10)
    #print(documents)
    rezepte = []
    for document in reversed(list(documents)):
        rezept_dict = {}
        rezept_dict['rezept'] = document['rezept']
        rezept_dict['zutaten'] = document['Zutaten']
        rezept_dict['Beschreibung'] = document['Beschreibung']
        rezepte.append(rezept_dict)
        
    return rezepte






#find
all = list(records.find({'name': 'Nudeln'}))
#print(all)
#create

# newdoc = {
#     'name': 'Nudeln',
#     'beschreibung': 'Nudeln mit Peste',
#     'Zutat 1' : 'Nudeln',
#     'Zutat 2' : 'Pesto',
# }

# records.insert_one(newdoc)
