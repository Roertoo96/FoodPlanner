from pymongo import MongoClient
from datetime import datetime
from FoodGenerator.views import *
import os


MONGOUSER = os.environ['MONGOUSER']
MONGOPW = os.environ['MONGOPW']
MONGOSERVER = os.environ['MONGOSERVER']



client = MongoClient(f"mongodb+srv://{MONGOUSER}:{MONGOPW}@{MONGOSERVER}/?retryWrites=true&w=majority")

db = client.get_database('rezepte_db')
records = db.rezepte_lastsearch
recordsrecipe = db.rezepte_records


def addlastsearch(rezept,name,ingredients,instructions,vorauswahl_filter):

    uploaddoc = {
        'rezept': name,
        'Zutaten': ingredients,
        'Beschreibung': instructions,
        'tags' : vorauswahl_filter,

    }
    records.insert_one(uploaddoc)
    
    return

def downloadlastadd():
    #print("in Download")
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

def downloadrecipe():
    #print("in Download Rezepte")
    documents = recordsrecipe.find()
    #print(documents)
    recipearry = []
    for document in documents:
        #print(document)
        
        rezept_dict = {}
        rezept_dict['rezept'] = document['rezept']
        rezept_dict['zutaten'] = document['Zutaten']
        rezept_dict['Beschreibung'] = document['Beschreibung']
        rezept_dict['tag'] = document['tag']
        recipearry.append(rezept_dict)
        
    return recipearry
    
    






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
